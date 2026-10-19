"""Funções que criam componentes visuais com o mesmo estilo.

Somente este arquivo importa as cores do tema. As telas usam funções como
criar_botao() e criar_campo(), evitando repetir a configuração visual.
"""

import customtkinter as ctk

import tema


def criar_tela(janela):
    """Cria o frame que ocupa a área principal da janela."""
    return ctk.CTkFrame(janela, fg_color=tema.COR_FUNDO)


def criar_frame_transparente(elemento_pai):
    """Cria um frame usado apenas para organizar outros componentes."""
    return ctk.CTkFrame(elemento_pai, fg_color="transparent")


def criar_card(elemento_pai, largura=None, altura=None):
    """Cria uma área branca com borda e cantos arredondados."""
    configuracao = {
        "fg_color": tema.COR_CARD,
        "border_width": 1,
        "border_color": tema.COR_BORDA,
        "corner_radius": 18,
    }

    if largura is not None:
        configuracao["width"] = largura
    if altura is not None:
        configuracao["height"] = altura

    # Os dois asteriscos transformam cada item do dicionário em um argumento
    # nomeado. Exemplo: {"width": 400} equivale a width=400.
    return ctk.CTkFrame(elemento_pai, **configuracao)


def criar_rotulo(
    elemento_pai,
    texto,
    tamanho=None,
    negrito=False,
    tipo_cor="texto",
    largura_quebra=None,
    alinhamento=None,
):
    """Cria um texto usando as configurações visuais do sistema."""
    cores_disponiveis = {
        "texto": tema.COR_TEXTO,
        "principal": tema.COR_PRINCIPAL,
        "destaque": tema.COR_DESTAQUE,
    }
    configuracao = {
        "text": texto,
        "text_color": cores_disponiveis[tipo_cor],
    }

    if tamanho is not None:
        peso = "bold" if negrito else "normal"
        configuracao["font"] = ctk.CTkFont(size=tamanho, weight=peso)
    if largura_quebra is not None:
        configuracao["wraplength"] = largura_quebra
    if alinhamento is not None:
        configuracao["justify"] = alinhamento

    return ctk.CTkLabel(elemento_pai, **configuracao)


def criar_campo(
    elemento_pai,
    texto_exemplo=None,
    senha=False,
    largura=None,
):
    """Cria um campo de entrada de texto."""
    configuracao = {
        "fg_color": tema.COR_CAMPO,
        "border_color": tema.COR_BORDA,
        "text_color": tema.COR_TEXTO,
    }

    if texto_exemplo is not None:
        configuracao["placeholder_text"] = texto_exemplo
    if senha:
        configuracao["show"] = "*"
    if largura is not None:
        configuracao["width"] = largura

    return ctk.CTkEntry(elemento_pai, **configuracao)


def criar_combo(elemento_pai, valores, valor_inicial):
    """Cria uma caixa de seleção e define seu primeiro valor."""
    combo = ctk.CTkComboBox(
        elemento_pai,
        values=valores,
        fg_color=tema.COR_CAMPO,
        border_color=tema.COR_BORDA,
        button_color=tema.COR_PRINCIPAL,
        button_hover_color=tema.COR_HOVER,
        text_color=tema.COR_TEXTO,
    )
    combo.set(valor_inicial)
    return combo


def criar_botao(
    elemento_pai,
    texto,
    comando,
    largura=None,
    secundario=False,
):
    """Cria um botão principal ou secundário."""
    cor_fundo = tema.COR_DESTAQUE if secundario else tema.COR_PRINCIPAL
    configuracao = {
        "text": texto,
        "fg_color": cor_fundo,
        "hover_color": tema.COR_HOVER,
        "text_color": tema.COR_TEXTO_CLARO,
        "command": comando,
    }

    if largura is not None:
        configuracao["width"] = largura

    return ctk.CTkButton(elemento_pai, **configuracao)


def criar_cabecalho(tela, titulo, voltar_ao_menu=None):
    """Adiciona o cabeçalho padrão a uma tela."""
    topo = criar_frame_transparente(tela)
    topo.pack(fill="x", padx=25, pady=(20, 10))

    if voltar_ao_menu is not None:
        criar_botao(
            topo,
            texto="← Menu",
            comando=voltar_ao_menu,
            largura=90,
        ).pack(side="left")

    criar_rotulo(
        topo,
        texto=titulo,
        tamanho=26,
        negrito=True,
    ).pack(side="left", padx=18)


def criar_campo_formulario(
    elemento_pai,
    texto,
    linha,
    coluna,
    margem_inferior=12,
):
    """Cria um rótulo e um campo nas posições informadas do formulário."""
    criar_rotulo(elemento_pai, texto).grid(
        row=linha,
        column=coluna,
        padx=15,
        pady=(12, 5),
        sticky="w",
    )

    campo = criar_campo(elemento_pai)
    campo.grid(
        row=linha + 1,
        column=coluna,
        padx=15,
        pady=(0, margem_inferior),
        sticky="ew",
    )
    return campo
