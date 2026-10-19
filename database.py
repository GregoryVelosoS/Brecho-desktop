"""Funções procedurais responsáveis pela comunicação com o MySQL."""

import mysql.connector
from mysql.connector import Error

from config import DB_CONFIG


def conectar():
    """Abre e devolve uma conexão usando os dados de config.py."""
    try:
        # ** transforma as opções do dicionário DB_CONFIG em argumentos da
        # função connect(), como host=..., user=... e password=....
        return mysql.connector.connect(
            **DB_CONFIG
        )
    except Error as erro:
        raise ConnectionError(
            f"Não foi possível conectar ao MySQL: {erro}"
        ) from erro


def inserir_cliente(nome, tipo):
    """Insere um cliente e devolve o código criado pelo MySQL."""
    # Os marcadores %s recebem os valores separadamente em cursor.execute().
    # Isso evita montar comandos SQL concatenando textos digitados pelo usuário.
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
        # commit confirma a alteração no banco de dados.
        conexao.commit()
        return cursor.lastrowid

    except Error as erro:
        # rollback desfaz a operação se o MySQL encontrar algum erro.
        conexao.rollback()
        raise RuntimeError(
            f"Erro ao salvar cliente: {erro}"
        ) from erro

    finally:
        # finally é executado com sucesso ou erro, garantindo o fechamento.
        cursor.close()
        conexao.close()


def inserir_produto(
    nome,
    tamanho,
    tipo_peca,
    preco
):
    """Insere um produto e devolve o código criado pelo MySQL."""
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
    produto,
    quantidade,
    preco_unitario,
    desconto_produto,
    subtotal,
    desconto_cliente,
    valor_final
):
    """Insere um pedido e devolve o código criado pelo MySQL."""
    sql = """
        INSERT INTO pedidos (
            cliente,
            tipo_cliente,
            produto,
            quantidade,
            preco_unitario,
            desconto_produto,
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
                produto,
                quantidade,
                preco_unitario,
                desconto_produto,
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
