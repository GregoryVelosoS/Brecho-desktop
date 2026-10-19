"""Funções do menu principal."""

from telas import componentes as ui


def criar_card_opcao(
    area_cards,
    coluna,
    titulo,
    descricao,
    texto_botao,
    comando,
):
    """Cria uma opção reutilizável do menu."""
    card = ui.criar_card(area_cards, altura=270)
    card.grid(row=0, column=coluna, padx=12, sticky="nsew")
    card.grid_propagate(False)

    ui.criar_rotulo(
        card,
        texto=titulo,
        tamanho=22,
        negrito=True,
    ).pack(pady=(35, 15))

    ui.criar_rotulo(
        card,
        texto=descricao,
        largura_quebra=220,
        alinhamento="center",
    ).pack(padx=20, pady=10)

    ui.criar_botao(
        card,
        texto=texto_botao,
        comando=comando,
    ).pack(pady=25)


def criar_tela_menu(janela, navegacao):
    """Monta o menu e devolve seu frame para app.py."""
    tela = ui.criar_tela(janela)
    ui.criar_cabecalho(tela, "Menu principal")

    ui.criar_rotulo(
        tela,
        texto="Escolha uma opção",
        tamanho=18,
    ).pack(pady=(15, 25))

    area_cards = ui.criar_frame_transparente(tela)
    area_cards.pack(fill="x", padx=80, pady=20)

    # As três colunas recebem o mesmo peso e dividem o espaço disponível.
    area_cards.grid_columnconfigure((0, 1, 2), weight=1)

    criar_card_opcao(
        area_cards,
        0,
        "Clientes",
        "Cadastre clientes do brechó.",
        "Cadastrar clientes",
        navegacao["clientes"],
    )
    criar_card_opcao(
        area_cards,
        1,
        "Produtos",
        "Cadastre produtos do brechó.",
        "Cadastrar produtos",
        navegacao["produtos"],
    )
    criar_card_opcao(
        area_cards,
        2,
        "Pedidos",
        "Cadastre pedidos do brechó.",
        "Cadastrar pedidos",
        navegacao["pedidos"],
    )

    ui.criar_botao(
        tela,
        texto="Sair",
        comando=navegacao["login"],
        largura=150,
    ).pack(pady=25)

    return tela
