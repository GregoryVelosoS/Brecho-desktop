"""Funções da tela de cadastro e cálculo de pedidos."""

from tkinter import messagebox

from database import inserir_pedido
from regras_negocio import calcular_pedido
from telas import componentes as ui


def ler_numeros(campos):
    """Converte e valida quantidade, preço e desconto digitados."""
    try:
        quantidade = int(campos["quantidade"].get())
        preco = float(campos["preco"].get())
        desconto_produto = float(campos["desconto_produto"].get())
    except ValueError as erro:
        # raise cria um erro com uma mensagem mais clara para quem usa o sistema.
        raise ValueError(
            "Quantidade, preço e desconto devem ser valores numéricos."
        ) from erro

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    if not 0 <= desconto_produto <= 100:
        raise ValueError("O desconto deve estar entre 0 e 100.")

    return quantidade, preco, desconto_produto


def calcular_valores_pedido(campos, resumo, estado):
    """Calcula o pedido e atualiza os textos de resumo na tela."""
    cliente = campos["cliente"].get().strip()
    produto = campos["produto"].get().strip()

    if not cliente or not produto:
        messagebox.showwarning(
            "Dados incompletos",
            "Informe o cliente e o produto.",
        )
        return

    try:
        quantidade, preco, desconto_produto = ler_numeros(campos)

        # A regra de negócio fica em outro arquivo porque não depende da tela.
        resultado = calcular_pedido(
            preco,
            quantidade,
            desconto_produto,
            campos["tipo_cliente"].get(),
        )
        estado["resultado"] = resultado

        subtotal, desconto_cliente, valor_final = resultado
        resumo["subtotal"].configure(text=f"Subtotal: R$ {subtotal:.2f}")
        resumo["desconto"].configure(
            text=f"Desconto da cliente: {desconto_cliente}%"
        )
        resumo["total"].configure(text=f"Valor final: R$ {valor_final:.2f}")
    except ValueError as erro:
        messagebox.showerror("Dados inválidos", str(erro))


def salvar_pedido(campos, resumo, estado):
    """Valida os dados calculados e solicita sua gravação no banco."""
    if estado["resultado"] is None:
        messagebox.showwarning(
            "Calcule primeiro",
            "Clique em Calcular antes de salvar.",
        )
        return

    cliente = campos["cliente"].get().strip()
    produto = campos["produto"].get().strip()

    if not cliente or not produto:
        messagebox.showwarning(
            "Dados incompletos",
            "Informe o cliente e o produto.",
        )
        return

    try:
        quantidade, preco, desconto_produto = ler_numeros(campos)
        subtotal, desconto_cliente, valor_final = estado["resultado"]

        codigo = inserir_pedido(
            cliente,
            campos["tipo_cliente"].get(),
            produto,
            quantidade,
            preco,
            desconto_produto,
            subtotal,
            desconto_cliente,
            valor_final,
        )
        messagebox.showinfo(
            "Pedido cadastrado",
            f"Pedido salvo com sucesso!\nCódigo: {codigo}",
        )
        limpar_pedido(campos, resumo, estado)
    except ValueError as erro:
        messagebox.showerror("Dados inválidos", str(erro))
    except (ConnectionError, RuntimeError) as erro:
        messagebox.showerror("Erro", str(erro))


def limpar_pedido(campos, resumo, estado):
    """Limpa os campos e restaura o resumo inicial."""
    nomes_campos_texto = (
        "cliente",
        "produto",
        "quantidade",
        "preco",
        "desconto_produto",
    )

    for nome_campo in nomes_campos_texto:
        campos[nome_campo].delete(0, "end")

    campos["tipo_cliente"].set("Novo")
    estado["resultado"] = None
    resumo["subtotal"].configure(text="Subtotal: R$ 0,00")
    resumo["desconto"].configure(text="Desconto da cliente: 0%")
    resumo["total"].configure(text="Valor final: R$ 0,00")


def criar_tela_pedidos(janela, navegacao):
    """Monta o formulário de pedidos e devolve seu frame para app.py."""
    tela = ui.criar_tela(janela)
    ui.criar_cabecalho(
        tela,
        "Cadastro de pedidos",
        navegacao["menu"],
    )

    corpo = ui.criar_card(tela)
    corpo.pack(fill="both", expand=True, padx=60, pady=25)
    corpo.grid_columnconfigure((0, 1), weight=1)

    campos = {
        "cliente": ui.criar_campo_formulario(corpo, "Cliente", 0, 0),
        "produto": ui.criar_campo_formulario(corpo, "Produto", 2, 0),
        "quantidade": ui.criar_campo_formulario(corpo, "Quantidade", 2, 1),
        "preco": ui.criar_campo_formulario(corpo, "Preço unitário", 4, 0),
        "desconto_produto": ui.criar_campo_formulario(
            corpo,
            "Desconto do produto (%)",
            4,
            1,
        ),
    }

    ui.criar_rotulo(corpo, "Tipo de cliente").grid(
        row=0,
        column=1,
        padx=15,
        pady=(12, 5),
        sticky="w",
    )
    campos["tipo_cliente"] = ui.criar_combo(
        corpo,
        ["Novo", "VIP"],
        "Novo",
    )
    campos["tipo_cliente"].grid(
        row=1,
        column=1,
        padx=15,
        pady=(0, 12),
        sticky="ew",
    )

    resumo = {
        "subtotal": ui.criar_rotulo(
            corpo,
            "Subtotal: R$ 0,00",
            tamanho=16,
            negrito=True,
        ),
        "desconto": ui.criar_rotulo(
            corpo,
            "Desconto da cliente: 0%",
        ),
        "total": ui.criar_rotulo(
            corpo,
            "Valor final: R$ 0,00",
            tamanho=18,
            negrito=True,
            tipo_cor="principal",
        ),
    }
    resumo["subtotal"].grid(
        row=6,
        column=0,
        padx=15,
        pady=(20, 8),
        sticky="w",
    )
    resumo["desconto"].grid(
        row=6,
        column=1,
        padx=15,
        pady=(20, 8),
        sticky="w",
    )
    resumo["total"].grid(
        row=7,
        column=0,
        columnspan=2,
        padx=15,
        pady=(5, 15),
        sticky="w",
    )

    # O dicionário estado guarda um valor que muda após o clique em Calcular.
    # Por ser mutável, as funções podem atualizar esse valor sem usar classes,
    # self ou uma variável global.
    estado = {"resultado": None}

    area_botoes = ui.criar_frame_transparente(corpo)
    area_botoes.grid(
        row=8,
        column=0,
        columnspan=2,
        padx=15,
        pady=(10, 25),
        sticky="ew",
    )
    area_botoes.grid_columnconfigure((0, 1, 2), weight=1)

    def ao_calcular():
        calcular_valores_pedido(campos, resumo, estado)

    def ao_salvar():
        salvar_pedido(campos, resumo, estado)

    def ao_limpar():
        limpar_pedido(campos, resumo, estado)

    ui.criar_botao(
        area_botoes,
        texto="Calcular",
        comando=ao_calcular,
    ).grid(row=0, column=0, padx=5, sticky="ew")

    ui.criar_botao(
        area_botoes,
        texto="Salvar pedido",
        comando=ao_salvar,
    ).grid(row=0, column=1, padx=5, sticky="ew")

    ui.criar_botao(
        area_botoes,
        texto="Limpar",
        comando=ao_limpar,
        secundario=True,
    ).grid(row=0, column=2, padx=5, sticky="ew")

    return tela
