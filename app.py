"""Ponto de entrada procedural do sistema do brechó."""

import customtkinter as ctk

import tema
from telas.clientes import criar_tela_clientes
from telas.login import criar_tela_login
from telas.menu import criar_tela_menu
from telas.pedidos import criar_tela_pedidos
from telas.produtos import criar_tela_produtos


# Estas variáveis começam vazias e recebem seus valores em iniciar_aplicacao().
# Elas ficam neste módulo porque todas as funções de navegação usam a mesma
# janela e precisam saber qual tela está sendo exibida no momento.
janela = None
frame_atual = None


def trocar_tela(funcao_criadora):
    """Remove a tela aberta e chama a função que cria a próxima tela."""
    global frame_atual

    if frame_atual is not None:
        frame_atual.destroy()

    # Uma função também pode ser recebida por parâmetro. Aqui chamamos a função
    # recebida e guardamos o frame que ela devolve com a palavra return.
    frame_atual = funcao_criadora(janela, navegacao)
    frame_atual.pack(fill="both", expand=True)


def abrir_login():
    """Abre a tela de login."""
    trocar_tela(criar_tela_login)


def abrir_menu():
    """Abre o menu principal."""
    trocar_tela(criar_tela_menu)


def abrir_clientes():
    """Abre o cadastro de clientes."""
    trocar_tela(criar_tela_clientes)


def abrir_produtos():
    """Abre o cadastro de produtos."""
    trocar_tela(criar_tela_produtos)


def abrir_pedidos():
    """Abre o cadastro de pedidos."""
    trocar_tela(criar_tela_pedidos)


# O dicionário relaciona um nome simples à função correspondente. Assim cada
# tela recebe somente este conjunto de opções, sem importar app.py e sem criar
# uma dependência circular entre os arquivos.
navegacao = {
    "login": abrir_login,
    "menu": abrir_menu,
    "clientes": abrir_clientes,
    "produtos": abrir_produtos,
    "pedidos": abrir_pedidos,
}


def iniciar_aplicacao():
    """Configura e inicia a janela principal."""
    global janela

    tema.configurar_tema()

    # CTk() cria a janela principal fornecida pela biblioteca CustomTkinter.
    # O projeto não cria classes próprias; apenas utiliza os componentes da
    # biblioteca, que internamente são objetos.
    janela = ctk.CTk()
    janela.title("Sistema do Brechó - UC2")
    janela.geometry("960x680")
    janela.minsize(860, 620)
    janela.configure(fg_color=tema.COR_FUNDO)

    abrir_login()

    # mainloop mantém a janela aberta e aguarda cliques e digitação.
    janela.mainloop()


if __name__ == "__main__":
    # Esta condição evita abrir a janela quando app.py for apenas importado.
    iniciar_aplicacao()
