# Protótipo UC2 — Sistema do Brechó

## Tecnologias
- Python
- CustomTkinter
- MySQL
- mysql-connector-python

## Escopo do protótipo
- Login local: admin / 1234
- Cadastro simples de pedido
- Cálculo reaproveitando a lógica da UC1
- Gravação do pedido no MySQL
- Tabelas: clientes, produtos e pedidos
- Sem relacionamentos nesta primeira versão

## Estrutura
```text
projeto_brecho_uc2/
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── README.md
└── sql/
    └── schema.sql
```

## Preparação
1. Execute `sql/schema.sql` no MySQL Workbench.
2. Ajuste usuário e senha em `config.py`.
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute:

```bash
python app.py
```

## Decisão pedagógica
Cada registro de `pedidos` representa um pedido simples com um produto.
A tabela guarda cliente e produto como texto, sem chaves estrangeiras.
Isso reduz a complexidade inicial de SQL e da integração Python/MySQL.

Depois da validação do protótipo, uma evolução possível é criar
relacionamentos e uma tabela `itens_pedido`.
# Brecho-desktop
