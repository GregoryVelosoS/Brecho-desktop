import customtkinter as ctk
from tkinter import messagebox

from database import (
    inserir_cliente,
    inserir_produto,
    inserir_pedido,
)


# =========================================================
# IDENTIDADE VISUAL DO SISTEMA
# =========================================================

# Define o modo de aparência do CustomTkinter.
# "light" mantém a interface clara.
ctk.set_appearance_mode("light")

# Mantém o tema-base azul apenas como referência interna da biblioteca.
# As principais cores da interface serão definidas manualmente abaixo.
ctk.set_default_color_theme("blue")


# Paleta de cores do Brechó.
# A vantagem de concentrar as cores aqui é que podemos alterar
# a identidade visual do sistema inteiro modificando poucos valores.
COR_FUNDO = "#F7F3EE"
COR_CARD = "#FFFFFF"
COR_PRINCIPAL = "#8B5E3C"
COR_HOVER = "#6F472D"
COR_DESTAQUE = "#C9A27E"
COR_TEXTO = "#2D2A26"
COR_TEXTO_CLARO = "#FFFFFF"
COR_BORDA = "#D8C3B0"
COR_CAMPO = "#FFFDFC"


# =========================================================
# FUNÇÕES DE REGRA DE NEGÓCIO
# =========================================================

def calcular_valor_produto(preco, quantidade, desconto_produto):
    """
    Calcula o valor de um produto após aplicar o desconto.

    Parâmetros:
        preco: preço unitário do produto.
        quantidade: quantidade comprada.
        desconto_produto: percentual de desconto do produto.

    Retorno:
        Valor final do produto após o desconto.
    """

    # Primeiro calculamos o valor bruto.
    valor_bruto = preco * quantidade

    # Depois calculamos quanto será descontado.
    valor_desconto = valor_bruto * desconto_produto / 100

    # Por fim, retiramos o desconto do valor bruto.
    return valor_bruto - valor_desconto


def obter_desconto_cliente(tipo):
    """
    Retorna o percentual de desconto conforme o tipo da cliente.

    Regras:
        Novo -> 5%
        VIP  -> 15%

    Se o tipo não for reconhecido, retorna 0%.
    """

    if tipo == "Novo":
        return 5

    elif tipo == "VIP":
        return 15

    return 0


def calcular_pedido(preco, quantidade, desconto_produto, tipo_cliente):
    """
    Calcula subtotal, desconto da cliente e valor final do pedido.

    A ordem usada é:
        1. desconto do produto;
        2. desconto da cliente;
        3. valor final.
    """

    # Calcula o valor do produto após o desconto individual.
    subtotal = calcular_valor_produto(
        preco,
        quantidade,
        desconto_produto
    )

    # Descobre o percentual da cliente.
    desconto_cliente = obter_desconto_cliente(
        tipo_cliente
    )

    # Calcula o valor final depois do desconto da cliente.
    valor_final = (
        subtotal
        - subtotal * desconto_cliente / 100
    )

    # Retorna três valores para serem usados na tela.
    return subtotal, desconto_cliente, valor_final


# =========================================================
# APLICAÇÃO PRINCIPAL
# =========================================================

class AplicacaoBrecho(ctk.CTk):
    """
    Janela principal do sistema.

    Esta classe controla a troca entre as telas:
        - Login
        - Menu
        - Clientes
        - Produtos
        - Pedidos
    """

    def __init__(self):
        """
        Construtor da aplicação.

        É executado automaticamente quando o programa é iniciado.
        """

        # Inicializa a janela principal do CustomTkinter.
        super().__init__()

        # Configura título e tamanho da janela.
        self.title("Sistema do Brechó - UC2")
        self.geometry("960x680")
        self.minsize(860, 620)

        # Define a cor principal do fundo da aplicação.
        self.configure(fg_color=COR_FUNDO)

        # Guarda a tela que está sendo exibida atualmente.
        self.frame_atual = None

        # O sistema sempre começa pela tela de login.
        self.abrir_login()

    def trocar_tela(self, classe_tela):
        """
        Remove a tela atual e abre uma nova tela.

        Recebe como parâmetro a classe da tela que deverá ser aberta.
        """

        # Se já existe uma tela aberta, ela é destruída.
        if self.frame_atual is not None:
            self.frame_atual.destroy()

        # Cria a nova tela.
        self.frame_atual = classe_tela(self)

        # Faz a nova tela ocupar todo o espaço da janela.
        self.frame_atual.pack(
            fill="both",
            expand=True
        )

    def abrir_login(self):
        """
        Abre a tela de login.
        """
        self.trocar_tela(TelaLogin)

    def abrir_menu(self):
        """
        Abre o menu principal.
        """
        self.trocar_tela(TelaMenu)

    def abrir_clientes(self):
        """
        Abre a tela de cadastro de clientes.
        """
        self.trocar_tela(TelaClientes)

    def abrir_produtos(self):
        """
        Abre a tela de cadastro de produtos.
        """
        self.trocar_tela(TelaProdutos)

    def abrir_pedidos(self):
        """
        Abre a tela de cadastro de pedidos.
        """
        self.trocar_tela(TelaPedidos)


# =========================================================
# TELA BASE
# =========================================================

class TelaBase(ctk.CTkFrame):
    """
    Classe-base usada pelas demais telas.

    Centraliza características visuais que serão repetidas
    em várias partes do sistema.
    """

    def __init__(self, master):
        """
        Inicializa a tela-base usando a cor de fundo padrão.
        """
        super().__init__(
            master,
            fg_color=COR_FUNDO
        )

    def cabecalho(self, titulo, voltar=True):
        """
        Cria o cabeçalho padrão das telas.

        Parâmetros:
            titulo: texto mostrado no topo.
            voltar: define se o botão "Menu" será exibido.
        """

        # Frame transparente usado apenas para organizar o cabeçalho.
        topo = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        topo.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        # Exibe botão para voltar ao menu quando necessário.
        if voltar:
            ctk.CTkButton(
                topo,
                text="← Menu",
                width=90,
                fg_color=COR_PRINCIPAL,
                hover_color=COR_HOVER,
                text_color=COR_TEXTO_CLARO,
                command=self.master.abrir_menu
            ).pack(side="left")

        # Título da tela.
        ctk.CTkLabel(
            topo,
            text=titulo,
            text_color=COR_TEXTO,
            font=ctk.CTkFont(
                size=26,
                weight="bold"
            )
        ).pack(
            side="left",
            padx=18
        )


# =========================================================
# TELA DE LOGIN
# =========================================================

class TelaLogin(TelaBase):
    """
    Tela inicial do sistema.

    Nesta versão didática, usuário e senha estão definidos
    diretamente no código, sem consulta ao banco de dados.
    """

    USUARIO = "admin"
    SENHA = "1234"

    def __init__(self, master):
        """
        Monta todos os elementos visuais da tela de login.
        """

        super().__init__(master)

        # Card central onde ficam os campos de login.
        card = ctk.CTkFrame(
            self,
            width=400,
            height=360,
            fg_color=COR_CARD,
            border_width=1,
            border_color=COR_BORDA,
            corner_radius=18
        )
        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        card.pack_propagate(False)

        # Título principal.
        ctk.CTkLabel(
            card,
            text="Sistema do Brechó",
            text_color=COR_TEXTO,
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        ).pack(
            pady=(45, 8)
        )

        # Texto de apoio.
        ctk.CTkLabel(
            card,
            text="Acesso ao sistema",
            text_color=COR_TEXTO
        ).pack(
            pady=(0, 20)
        )

        # Campo para usuário.
        self.usuario = ctk.CTkEntry(
            card,
            placeholder_text="Usuário",
            width=290,
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            text_color=COR_TEXTO
        )
        self.usuario.pack(pady=8)

        # Campo para senha.
        self.senha = ctk.CTkEntry(
            card,
            placeholder_text="Senha",
            show="*",
            width=290,
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            text_color=COR_TEXTO
        )
        self.senha.pack(pady=8)

        # Botão de entrada.
        ctk.CTkButton(
            card,
            text="Entrar",
            width=290,
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.validar
        ).pack(
            pady=(18, 8)
        )

        # Informação de acesso para o protótipo didático.
        ctk.CTkLabel(
            card,
            text="Acesso didático: admin / 1234",
            text_color=COR_DESTAQUE
        ).pack()

        # Permite pressionar Enter após digitar a senha.
        self.senha.bind(
            "<Return>",
            lambda event: self.validar()
        )

    def validar(self):
        """
        Compara usuário e senha digitados com os valores definidos
        diretamente na classe.

        Se estiverem corretos, abre o menu.
        Caso contrário, mostra uma mensagem de erro.
        """

        if (
            self.usuario.get() == self.USUARIO
            and self.senha.get() == self.SENHA
        ):
            self.master.abrir_menu()

        else:
            messagebox.showerror(
                "Acesso negado",
                "Usuário ou senha incorretos."
            )


# =========================================================
# MENU PRINCIPAL
# =========================================================

class TelaMenu(TelaBase):
    """
    Tela apresentada após o login.

    Oferece acesso aos três cadastros principais do sistema.
    """

    def __init__(self, master):
        """
        Cria os três cards do menu principal.
        """

        super().__init__(master)

        self.cabecalho(
            "Menu principal",
            voltar=False
        )

        ctk.CTkLabel(
            self,
            text="Escolha uma opção",
            text_color=COR_TEXTO,
            font=ctk.CTkFont(size=18)
        ).pack(
            pady=(15, 25)
        )

        # Área onde ficarão os três cards.
        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards.pack(
            fill="x",
            padx=80,
            pady=20
        )

        # Faz os três cards ocuparem espaços semelhantes.
        cards.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        # Card de clientes.
        self.criar_card(
            cards,
            0,
            "Clientes",
            "Cadastre clientes do brechó.",
            "Cadastrar clientes",
            master.abrir_clientes
        )

        # Card de produtos.
        self.criar_card(
            cards,
            1,
            "Produtos",
            "Cadastre produtos do brechó.",
            "Cadastrar produtos",
            master.abrir_produtos
        )

        # Card de pedidos.
        self.criar_card(
            cards,
            2,
            "Pedidos",
            "Cadastre pedidos do brechó.",
            "Cadastrar pedidos",
            master.abrir_pedidos
        )

        # Botão para retornar ao login.
        ctk.CTkButton(
            self,
            text="Sair",
            width=150,
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=master.abrir_login
        ).pack(
            pady=25
        )

    def criar_card(
        self,
        master,
        coluna,
        titulo,
        descricao,
        texto_botao,
        comando
    ):
        """
        Cria um card reutilizável no menu.

        Isso evita repetir todo o código de construção visual
        para Clientes, Produtos e Pedidos.
        """

        card = ctk.CTkFrame(
            master,
            height=270,
            fg_color=COR_CARD,
            border_width=1,
            border_color=COR_BORDA,
            corner_radius=18
        )

        card.grid(
            row=0,
            column=coluna,
            padx=12,
            sticky="nsew"
        )

        # Impede que o conteúdo altere o tamanho definido do card.
        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=titulo,
            text_color=COR_TEXTO,
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        ).pack(
            pady=(35, 15)
        )

        ctk.CTkLabel(
            card,
            text=descricao,
            text_color=COR_TEXTO,
            wraplength=220,
            justify="center"
        ).pack(
            padx=20,
            pady=10
        )

        ctk.CTkButton(
            card,
            text=texto_botao,
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=comando
        ).pack(
            pady=25
        )


# =========================================================
# CADASTRO DE CLIENTES
# =========================================================

class TelaClientes(TelaBase):
    """
    Tela destinada ao cadastro de clientes.
    """

    def __init__(self, master):
        """
        Cria os campos Nome e Tipo de cliente.
        """

        super().__init__(master)

        self.cabecalho(
            "Cadastro de clientes"
        )

        corpo = ctk.CTkFrame(
            self,
            fg_color=COR_CARD,
            border_width=1,
            border_color=COR_BORDA,
            corner_radius=18
        )
        corpo.pack(
            fill="x",
            padx=80,
            pady=35
        )

        corpo.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        ctk.CTkLabel(
            corpo,
            text="Nome da cliente",
            text_color=COR_TEXTO
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=(25, 5),
            sticky="w"
        )

        self.nome = ctk.CTkEntry(
            corpo,
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            text_color=COR_TEXTO
        )
        self.nome.grid(
            row=1,
            column=0,
            padx=15,
            pady=(0, 20),
            sticky="ew"
        )

        ctk.CTkLabel(
            corpo,
            text="Tipo de cliente",
            text_color=COR_TEXTO
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=(25, 5),
            sticky="w"
        )

        self.tipo = ctk.CTkComboBox(
            corpo,
            values=["Novo", "VIP"],
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            button_color=COR_PRINCIPAL,
            button_hover_color=COR_HOVER,
            text_color=COR_TEXTO
        )
        self.tipo.set("Novo")
        self.tipo.grid(
            row=1,
            column=1,
            padx=15,
            pady=(0, 20),
            sticky="ew"
        )

        ctk.CTkButton(
            corpo,
            text="Salvar cliente",
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.salvar
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            padx=15,
            pady=(5, 25),
            sticky="ew"
        )

    def salvar(self):
        """
        Valida os dados preenchidos e envia o cadastro para
        a função inserir_cliente(), localizada em database.py.
        """

        nome = self.nome.get().strip()
        tipo = self.tipo.get()

        # Não permite salvar um cliente sem nome.
        if not nome:
            messagebox.showwarning(
                "Dados incompletos",
                "Informe o nome da cliente."
            )
            return

        try:
            codigo = inserir_cliente(
                nome,
                tipo
            )

            messagebox.showinfo(
                "Cliente cadastrado",
                (
                    "Cliente salvo com sucesso!\n"
                    f"Código: {codigo}"
                )
            )

            # Limpa os campos após salvar.
            self.nome.delete(
                0,
                "end"
            )
            self.tipo.set("Novo")

        except (
            ConnectionError,
            RuntimeError
        ) as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )


# =========================================================
# CADASTRO DE PRODUTOS
# =========================================================

class TelaProdutos(TelaBase):
    """
    Tela destinada ao cadastro dos produtos do brechó.
    """

    def __init__(self, master):
        """
        Monta o formulário de produtos.
        """

        super().__init__(master)

        self.cabecalho(
            "Cadastro de produtos"
        )

        corpo = ctk.CTkFrame(
            self,
            fg_color=COR_CARD,
            border_width=1,
            border_color=COR_BORDA,
            corner_radius=18
        )
        corpo.pack(
            fill="x",
            padx=80,
            pady=35
        )

        corpo.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.nome = self.criar_campo(
            corpo,
            "Nome do produto",
            0,
            0
        )

        self.tamanho = self.criar_campo(
            corpo,
            "Tamanho",
            0,
            1
        )

        ctk.CTkLabel(
            corpo,
            text="Tipo de peça",
            text_color=COR_TEXTO
        ).grid(
            row=2,
            column=0,
            padx=15,
            pady=(12, 5),
            sticky="w"
        )

        self.tipo_peca = ctk.CTkComboBox(
            corpo,
            values=[
                "Roupas",
                "Calçados",
                "Bolsas",
                "Acessórios",
                "Jóias e bijuterias",
                "Outros"
            ],
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            button_color=COR_PRINCIPAL,
            button_hover_color=COR_HOVER,
            text_color=COR_TEXTO
        )
        self.tipo_peca.set("Roupas")
        self.tipo_peca.grid(
            row=3,
            column=0,
            padx=15,
            pady=(0, 20),
            sticky="ew"
        )

        self.preco = self.criar_campo(
            corpo,
            "Preço",
            2,
            1
        )

        ctk.CTkButton(
            corpo,
            text="Salvar produto",
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.salvar
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            padx=15,
            pady=(15, 25),
            sticky="ew"
        )

    def criar_campo(
        self,
        master,
        texto,
        linha,
        coluna
    ):
        """
        Cria um rótulo e um campo de entrada.

        Esta função existe para evitar repetição de código
        na construção do formulário de produtos.
        """

        ctk.CTkLabel(
            master,
            text=texto,
            text_color=COR_TEXTO
        ).grid(
            row=linha,
            column=coluna,
            padx=15,
            pady=(12, 5),
            sticky="w"
        )

        campo = ctk.CTkEntry(
            master,
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            text_color=COR_TEXTO
        )
        campo.grid(
            row=linha + 1,
            column=coluna,
            padx=15,
            pady=(0, 20),
            sticky="ew"
        )

        return campo

    def salvar(self):
        """
        Valida os dados e salva o produto no banco.
        """

        nome = self.nome.get().strip()
        tamanho = self.tamanho.get().strip()
        tipo_peca = self.tipo_peca.get()

        if not nome:
            messagebox.showwarning(
                "Dados incompletos",
                "Informe o nome do produto."
            )
            return

        try:
            # Converte o preço digitado para número decimal.
            preco = float(
                self.preco.get()
            )

            if preco < 0:
                raise ValueError(
                    "O preço não pode ser negativo."
                )

            codigo = inserir_produto(
                nome,
                tamanho,
                tipo_peca,
                preco
            )

            messagebox.showinfo(
                "Produto cadastrado",
                (
                    "Produto salvo com sucesso!\n"
                    f"Código: {codigo}"
                )
            )

            # Limpa os campos após o cadastro.
            for campo in (
                self.nome,
                self.tamanho,
                self.preco
            ):
                campo.delete(
                    0,
                    "end"
                )

            self.tipo_peca.set("Roupas")

        except ValueError as erro:
            messagebox.showerror(
                "Dados inválidos",
                str(erro)
            )

        except (
            ConnectionError,
            RuntimeError
        ) as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )


# =========================================================
# CADASTRO DE PEDIDOS
# =========================================================

class TelaPedidos(TelaBase):
    """
    Tela destinada ao cadastro de pedidos.

    Nesta versão, o pedido trabalha com um produto por registro,
    mantendo a estrutura simples do protótipo.
    """

    def __init__(self, master):
        """
        Monta os campos, resumo do pedido e botões de ação.
        """

        super().__init__(master)

        self.cabecalho(
            "Cadastro de pedidos"
        )

        corpo = ctk.CTkFrame(
            self,
            fg_color=COR_CARD,
            border_width=1,
            border_color=COR_BORDA,
            corner_radius=18
        )
        corpo.pack(
            fill="both",
            expand=True,
            padx=60,
            pady=25
        )

        corpo.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        self.cliente = self.criar_campo(
            corpo,
            "Cliente",
            0,
            0
        )

        ctk.CTkLabel(
            corpo,
            text="Tipo de cliente",
            text_color=COR_TEXTO
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=(12, 5),
            sticky="w"
        )

        self.tipo_cliente = ctk.CTkComboBox(
            corpo,
            values=["Novo", "VIP"],
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            button_color=COR_PRINCIPAL,
            button_hover_color=COR_HOVER,
            text_color=COR_TEXTO
        )
        self.tipo_cliente.set("Novo")
        self.tipo_cliente.grid(
            row=1,
            column=1,
            padx=15,
            pady=(0, 12),
            sticky="ew"
        )

        self.produto = self.criar_campo(
            corpo,
            "Produto",
            2,
            0
        )

        self.quantidade = self.criar_campo(
            corpo,
            "Quantidade",
            2,
            1
        )

        self.preco = self.criar_campo(
            corpo,
            "Preço unitário",
            4,
            0
        )

        self.desconto_produto = self.criar_campo(
            corpo,
            "Desconto do produto (%)",
            4,
            1
        )

        self.lbl_subtotal = ctk.CTkLabel(
            corpo,
            text="Subtotal: R$ 0,00",
            text_color=COR_TEXTO,
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )
        )
        self.lbl_subtotal.grid(
            row=6,
            column=0,
            padx=15,
            pady=(20, 8),
            sticky="w"
        )

        self.lbl_desconto = ctk.CTkLabel(
            corpo,
            text="Desconto da cliente: 0%",
            text_color=COR_TEXTO
        )
        self.lbl_desconto.grid(
            row=6,
            column=1,
            padx=15,
            pady=(20, 8),
            sticky="w"
        )

        self.lbl_total = ctk.CTkLabel(
            corpo,
            text="Valor final: R$ 0,00",
            text_color=COR_PRINCIPAL,
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )
        self.lbl_total.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=15,
            pady=(5, 15),
            sticky="w"
        )

        # Área dos três botões.
        botoes = ctk.CTkFrame(
            corpo,
            fg_color="transparent"
        )
        botoes.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=15,
            pady=(10, 25),
            sticky="ew"
        )

        botoes.grid_columnconfigure(
            (0, 1, 2),
            weight=1
        )

        ctk.CTkButton(
            botoes,
            text="Calcular",
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.calcular
        ).grid(
            row=0,
            column=0,
            padx=5,
            sticky="ew"
        )

        ctk.CTkButton(
            botoes,
            text="Salvar pedido",
            fg_color=COR_PRINCIPAL,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.salvar
        ).grid(
            row=0,
            column=1,
            padx=5,
            sticky="ew"
        )

        ctk.CTkButton(
            botoes,
            text="Limpar",
            fg_color=COR_DESTAQUE,
            hover_color=COR_HOVER,
            text_color=COR_TEXTO_CLARO,
            command=self.limpar
        ).grid(
            row=0,
            column=2,
            padx=5,
            sticky="ew"
        )

        # Guarda o último cálculo realizado.
        self.resultado = None

    def criar_campo(
        self,
        master,
        texto,
        linha,
        coluna
    ):
        """
        Cria um rótulo e um campo de entrada
        para o formulário de pedidos.
        """

        ctk.CTkLabel(
            master,
            text=texto,
            text_color=COR_TEXTO
        ).grid(
            row=linha,
            column=coluna,
            padx=15,
            pady=(12, 5),
            sticky="w"
        )

        campo = ctk.CTkEntry(
            master,
            fg_color=COR_CAMPO,
            border_color=COR_BORDA,
            text_color=COR_TEXTO
        )
        campo.grid(
            row=linha + 1,
            column=coluna,
            padx=15,
            pady=(0, 12),
            sticky="ew"
        )

        return campo

    def ler_numeros(self):
        """
        Lê e valida os campos numéricos do pedido.

        Retorna:
            quantidade, preço e desconto do produto.
        """

        try:
            quantidade = int(
                self.quantidade.get()
            )

            preco = float(
                self.preco.get()
            )

            desconto_produto = float(
                self.desconto_produto.get()
            )

        except ValueError:
            raise ValueError(
                "Quantidade, preço e desconto "
                "devem ser valores numéricos."
            )

        if quantidade <= 0:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        if preco < 0:
            raise ValueError(
                "O preço não pode ser negativo."
            )

        if not 0 <= desconto_produto <= 100:
            raise ValueError(
                "O desconto deve estar entre 0 e 100."
            )

        return (
            quantidade,
            preco,
            desconto_produto
        )

    def calcular(self):
        """
        Calcula os valores do pedido e atualiza o resumo na tela.
        """

        cliente = self.cliente.get().strip()
        produto = self.produto.get().strip()

        # Cliente e produto são obrigatórios.
        if not cliente or not produto:
            messagebox.showwarning(
                "Dados incompletos",
                "Informe o cliente e o produto."
            )
            return

        try:
            (
                quantidade,
                preco,
                desconto_produto
            ) = self.ler_numeros()

            (
                subtotal,
                desconto_cliente,
                valor_final
            ) = calcular_pedido(
                preco,
                quantidade,
                desconto_produto,
                self.tipo_cliente.get()
            )

            # Armazena o resultado para depois salvar no banco.
            self.resultado = (
                subtotal,
                desconto_cliente,
                valor_final
            )

            # Atualiza os textos apresentados na interface.
            self.lbl_subtotal.configure(
                text=f"Subtotal: R$ {subtotal:.2f}"
            )

            self.lbl_desconto.configure(
                text=(
                    "Desconto da cliente: "
                    f"{desconto_cliente}%"
                )
            )

            self.lbl_total.configure(
                text=f"Valor final: R$ {valor_final:.2f}"
            )

        except ValueError as erro:
            messagebox.showerror(
                "Dados inválidos",
                str(erro)
            )

    def salvar(self):
        """
        Salva o pedido no banco de dados.

        Antes de salvar, exige que o cálculo tenha sido realizado.
        """

        # Impede salvar um pedido ainda não calculado.
        if self.resultado is None:
            messagebox.showwarning(
                "Calcule primeiro",
                "Clique em Calcular antes de salvar."
            )
            return

        cliente = self.cliente.get().strip()
        produto = self.produto.get().strip()

        if not cliente or not produto:
            messagebox.showwarning(
                "Dados incompletos",
                "Informe o cliente e o produto."
            )
            return

        try:
            (
                quantidade,
                preco,
                desconto_produto
            ) = self.ler_numeros()

            (
                subtotal,
                desconto_cliente,
                valor_final
            ) = self.resultado

            # Envia os dados para database.py.
            codigo = inserir_pedido(
                cliente,
                self.tipo_cliente.get(),
                produto,
                quantidade,
                preco,
                desconto_produto,
                subtotal,
                desconto_cliente,
                valor_final
            )

            messagebox.showinfo(
                "Pedido cadastrado",
                (
                    "Pedido salvo com sucesso!\n"
                    f"Código: {codigo}"
                )
            )

            # Limpa a tela após o cadastro.
            self.limpar()

        except ValueError as erro:
            messagebox.showerror(
                "Dados inválidos",
                str(erro)
            )

        except (
            ConnectionError,
            RuntimeError
        ) as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def limpar(self):
        """
        Limpa todos os campos e restaura os valores iniciais da tela.
        """

        for campo in (
            self.cliente,
            self.produto,
            self.quantidade,
            self.preco,
            self.desconto_produto
        ):
            campo.delete(
                0,
                "end"
            )

        self.tipo_cliente.set("Novo")

        # Apaga o último resultado calculado.
        self.resultado = None

        # Restaura os textos do resumo.
        self.lbl_subtotal.configure(
            text="Subtotal: R$ 0,00"
        )

        self.lbl_desconto.configure(
            text="Desconto da cliente: 0%"
        )

        self.lbl_total.configure(
            text="Valor final: R$ 0,00"
        )


# =========================================================
# INÍCIO DO PROGRAMA
# =========================================================

if __name__ == "__main__":
    # Cria a aplicação.
    app = AplicacaoBrecho()

    # Mantém a janela aberta aguardando as ações da usuária.
    app.mainloop()
