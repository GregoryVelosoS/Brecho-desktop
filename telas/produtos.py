"""Funções da tela de cadastro de produtos."""

from tkinter import messagebox

from database import inserir_produto
from telas import componentes as ui


def salvar_produto(campos):
    """Valida os campos e solicita a gravação do produto no banco."""
    nome = campos["nome"].get().strip()
    tamanho = campos["tamanho"].get().strip()
    tipo_peca = campos["tipo_peca"].get()

    if not nome:
        messagebox.showwarning(
            "Dados incompletos",
            "Informe o nome do produto.",
        )
        return

    try:
        # float converte o texto digitado em um número que aceita casas decimais.
        preco = float(campos["preco"].get())
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        codigo = inserir_produto(nome, tamanho, tipo_peca, preco)
        messagebox.showinfo(
            "Produto cadastrado",
            f"Produto salvo com sucesso!\nCódigo: {codigo}",
        )

        for nome_campo in ("nome", "tamanho", "preco"):
            campos[nome_campo].delete(0, "end")
        campos["tipo_peca"].set("Roupas")
    except ValueError as erro:
        messagebox.showerror("Dados inválidos", str(erro))
    except (ConnectionError, RuntimeError) as erro:
        messagebox.showerror("Erro", str(erro))


def criar_tela_produtos(janela, navegacao):
    """Monta o formulário de produtos e devolve seu frame para app.py."""
    tela = ui.criar_tela(janela)
    ui.criar_cabecalho(
        tela,
        "Cadastro de produtos",
        navegacao["menu"],
    )

    corpo = ui.criar_card(tela)
    corpo.pack(fill="x", padx=80, pady=35)
    corpo.grid_columnconfigure((0, 1), weight=1)

    # Este dicionário agrupa os campos pelo nome. Assim as funções recebem um
    # único parâmetro em vez de uma lista extensa de parâmetros separados.
    campos = {
        "nome": ui.criar_campo_formulario(
            corpo,
            "Nome do produto",
            0,
            0,
            margem_inferior=20,
        ),
        "tamanho": ui.criar_campo_formulario(
            corpo,
            "Tamanho",
            0,
            1,
            margem_inferior=20,
        ),
    }

    ui.criar_rotulo(corpo, "Tipo de peça").grid(
        row=2,
        column=0,
        padx=15,
        pady=(12, 5),
        sticky="w",
    )
    campos["tipo_peca"] = ui.criar_combo(
        corpo,
        [
            "Roupas",
            "Calçados",
            "Bolsas",
            "Acessórios",
            "Jóias e bijuterias",
            "Outros",
        ],
        "Roupas",
    )
    campos["tipo_peca"].grid(
        row=3,
        column=0,
        padx=15,
        pady=(0, 20),
        sticky="ew",
    )

    campos["preco"] = ui.criar_campo_formulario(
        corpo,
        "Preço",
        2,
        1,
        margem_inferior=20,
    )

    def ao_salvar():
        salvar_produto(campos)

    ui.criar_botao(
        corpo,
        texto="Salvar produto",
        comando=ao_salvar,
    ).grid(
        row=4,
        column=0,
        columnspan=2,
        padx=15,
        pady=(15, 25),
        sticky="ew",
    )

    return tela
