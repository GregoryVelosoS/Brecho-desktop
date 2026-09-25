CREATE DATABASE IF NOT EXISTS brecho_uc2;

USE brecho_uc2;


-- =========================================================
-- CLIENTES
-- Cadastro independente.
-- =========================================================

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL
);


-- =========================================================
-- PRODUTOS
-- Cadastro independente.
-- =========================================================

CREATE TABLE IF NOT EXISTS produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tamanho VARCHAR(20),
    tipo_peca VARCHAR(50),
    preco DECIMAL(10,2) NOT NULL
);


-- =========================================================
-- PEDIDOS
-- Cadastro independente.
-- Cliente e produto são gravados como texto.
-- =========================================================

CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(20) NOT NULL,
    produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    desconto_produto DECIMAL(5,2) DEFAULT 0,
    subtotal DECIMAL(10,2) NOT NULL,
    desconto_cliente DECIMAL(5,2) DEFAULT 0,
    valor_final DECIMAL(10,2) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
