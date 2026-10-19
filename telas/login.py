"""Funções da tela de login."""

from tkinter import messagebox

from telas import componentes as ui


USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"


def validar_login(campo_usuario, campo_senha, abrir_menu):
    """Compara os valores digitados e abre o menu quando estiverem corretos."""
    usuario_digitado = campo_usuario.get()
    senha_digitada = campo_senha.get()

    if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
        abrir_menu()
        return

    messagebox.showerror(
        "Acesso negado",
        "Usuário ou senha incorretos.",
    )


def criar_tela_login(janela, navegacao):
    """Monta a tela de login e devolve seu frame para app.py."""
    tela = ui.criar_tela(janela)
    card = ui.criar_card(tela, largura=400, altura=360)
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)

    ui.criar_rotulo(
        card,
        texto="Sistema do Brechó",
        tamanho=28,
        negrito=True,
    ).pack(pady=(45, 8))

    ui.criar_rotulo(card, "Acesso ao sistema").pack(pady=(0, 20))

    campo_usuario = ui.criar_campo(
        card,
        texto_exemplo="Usuário",
        largura=290,
    )
    campo_usuario.pack(pady=8)

    campo_senha = ui.criar_campo(
        card,
        texto_exemplo="Senha",
        senha=True,
        largura=290,
    )
    campo_senha.pack(pady=8)

    # command precisa receber uma função, e não o resultado de uma função.
    # Esta função interna chama validar_login() com os campos desta tela.
    def tentar_entrar():
        validar_login(
            campo_usuario,
            campo_senha,
            navegacao["menu"],
        )

    ui.criar_botao(
        card,
        texto="Entrar",
        comando=tentar_entrar,
        largura=290,
    ).pack(pady=(18, 8))

    ui.criar_rotulo(
        card,
        texto="Acesso didático: admin / 1234",
        tipo_cor="destaque",
    ).pack()

    # O parâmetro event recebe informações sobre a tecla pressionada. Ele não
    # é usado aqui, mas precisa existir para o bind funcionar.
    def pressionar_enter(event):
        tentar_entrar()

    campo_senha.bind("<Return>", pressionar_enter)
    return tela
