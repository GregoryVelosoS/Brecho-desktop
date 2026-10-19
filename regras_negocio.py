"""Regras de cálculo independentes da interface gráfica."""


def calcular_valor_produto(preco, quantidade, desconto_produto):
    """Calcula o valor de um produto após aplicar seu desconto."""
    # Cada função recebe os dados por parâmetros e devolve o resultado com
    # return. Por isso ela pode ser usada sem depender da interface gráfica.
    valor_bruto = preco * quantidade
    valor_desconto = valor_bruto * desconto_produto / 100
    return valor_bruto - valor_desconto


def obter_desconto_cliente(tipo):
    """Retorna o percentual de desconto conforme o tipo de cliente."""
    if tipo == "Novo":
        return 5

    if tipo == "VIP":
        return 15

    return 0


def calcular_pedido(preco, quantidade, desconto_produto, tipo_cliente):
    """Calcula subtotal, desconto do cliente e valor final do pedido."""
    # Reutilizamos funções menores para não repetir as mesmas fórmulas.
    subtotal = calcular_valor_produto(
        preco,
        quantidade,
        desconto_produto,
    )
    desconto_cliente = obter_desconto_cliente(tipo_cliente)
    valor_final = subtotal - subtotal * desconto_cliente / 100

    return subtotal, desconto_cliente, valor_final
