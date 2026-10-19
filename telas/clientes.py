"""Funções da tela de cadastro de clientes."""

from tkinter import messagebox

from database import inserir_cliente
from telas import componentes as ui


def salvar_cliente(campo_nome, campo_tipo):
    """Valida os campos e solicita a gravação do cliente no banco."""
    nome = campo_nome.get().strip()
    tipo = campo_tipo.get()

    if not nome:
        messagebox.showwarning(
            "Dados incompletos",
            "Informe o nome da cliente.",
        )
        return

    try:
        codigo = inserir_cliente(nome, tipo)
        messagebox.showinfo(
            "Cliente cadastrado",
            f"Cliente salvo com sucesso!\nCódigo: {codigo}",
        )

        # delete(0, "end") apaga o conteúdo do primeiro ao último caractere.
        campo_nome.delete(0, "end")
        campo_tipo.set("Novo")
    except (ConnectionError, RuntimeError) as erro:
        messagebox.showerror("Erro", str(erro))


def criar_tela_clientes(janela, navegacao):
    """Monta o formulário de clientes e devolve seu frame para app.py."""
    tela = ui.criar_tela(janela)
    ui.criar_cabecalho(
        tela,
        "Cadastro de clientes",
        navegacao["menu"],
    )

    corpo = ui.criar_card(tela)
    corpo.pack(fill="x", padx=80, pady=35)
    corpo.grid_columnconfigure((0, 1), weight=1)

    ui.criar_rotulo(corpo, "Nome da cliente").grid(
        row=0,
        column=0,
        padx=15,
        pady=(25, 5),
        sticky="w",
    )
    campo_nome = ui.criar_campo(corpo)
    campo_nome.grid(
        row=1,
        column=0,
        padx=15,
        pady=(0, 20),
        sticky="ew",
    )

    ui.criar_rotulo(corpo, "Tipo de cliente").grid(
        row=0,
        column=1,
        padx=15,
        pady=(25, 5),
        sticky="w",
    )
    campo_tipo = ui.criar_combo(corpo, ["Novo", "VIP"], "Novo")
    campo_tipo.grid(
        row=1,
        column=1,
        padx=15,
        pady=(0, 20),
        sticky="ew",
    )

    def ao_salvar():
        salvar_cliente(campo_nome, campo_tipo)

    ui.criar_botao(
        corpo,
        texto="Salvar cliente",
        comando=ao_salvar,
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        padx=15,
        pady=(5, 25),
        sticky="ew",
    )

    return tela
