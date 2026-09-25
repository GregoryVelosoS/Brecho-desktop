import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG


def conectar():
    try:
        return mysql.connector.connect(
            **DB_CONFIG
        )
    except Error as erro:
        raise ConnectionError(
            f"Não foi possível conectar ao MySQL: {erro}"
        ) from erro


def inserir_cliente(nome, tipo):
    sql = """
        INSERT INTO clientes (
            nome,
            tipo
        )
        VALUES (%s, %s)
    """

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            sql,
            (nome, tipo)
        )
        conexao.commit()
        return cursor.lastrowid

    except Error as erro:
        conexao.rollback()
        raise RuntimeError(
            f"Erro ao salvar cliente: {erro}"
        ) from erro

    finally:
        cursor.close()
        conexao.close()


def inserir_produto(
    nome,
    tamanho,
    tipo_peca,
    preco
):
    sql = """
        INSERT INTO produtos (
            nome,
            tamanho,
            tipo_peca,
            preco
        )
        VALUES (%s, %s, %s, %s)
    """

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            sql,
            (
                nome,
                tamanho,
                tipo_peca,
                preco
            )
        )
        conexao.commit()
        return cursor.lastrowid

    except Error as erro:
        conexao.rollback()
        raise RuntimeError(
            f"Erro ao salvar produto: {erro}"
        ) from erro

    finally:
        cursor.close()
        conexao.close()


def inserir_pedido(
    cliente,
    tipo_cliente,
    produtos,
    quantidades,
    precos,
    descontos_produtos,
    subtotal,
    desconto_cliente,
    valor_final
):
    sql = """
        INSERT INTO pedidos (
            cliente,
            tipo_cliente,
            produtos,
            quantidades,
            precos,
            descontos_produtos,
            subtotal,
            desconto_cliente,
            valor_final
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            sql,
            (
                cliente,
                tipo_cliente,
                produtos,
                quantidades,
                precos,
                descontos_produtos,
                subtotal,
                desconto_cliente,
                valor_final
            )
        )

        conexao.commit()
        return cursor.lastrowid

    except Error as erro:
        conexao.rollback()
        raise RuntimeError(
            f"Erro ao salvar pedido: {erro}"
        ) from erro

    finally:
        cursor.close()
        conexao.close()
