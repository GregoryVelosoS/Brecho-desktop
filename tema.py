"""Configuração visual compartilhada por todas as telas."""

import customtkinter as ctk


# As constantes abaixo formam a paleta do sistema. Como as cores ficam em um
# único arquivo, uma troca de identidade visual não exige alterar cada tela.
COR_FUNDO = "#F7F3EE"
COR_CARD = "#FFFFFF"
COR_PRINCIPAL = "#8B5E3C"
COR_HOVER = "#6F472D"
COR_DESTAQUE = "#C9A27E"
COR_TEXTO = "#2D2A26"
COR_TEXTO_CLARO = "#FFFFFF"
COR_BORDA = "#D8C3B0"
COR_CAMPO = "#FFFDFC"


def configurar_tema():
    """Aplica o modo e o tema-base usados pela aplicação."""
    # Estas funções precisam ser chamadas antes da criação da janela principal.
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
