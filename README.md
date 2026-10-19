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
├── regras_negocio.py
├── requirements.txt
├── README.md
├── tema.py
├── telas/
│   ├── __init__.py
│   ├── clientes.py
│   ├── componentes.py
│   ├── login.py
│   ├── menu.py
│   ├── pedidos.py
│   └── produtos.py
└── sql/
    └── schema.sql
```

## Organização do código

- `app.py`: inicia a janela e controla a navegação com funções;
- `tema.py`: concentra cores e configuração visual;
- `regras_negocio.py`: contém os cálculos de descontos e pedidos;
- `telas/componentes.py`: cria campos, botões, cards e cabeçalhos padronizados;
- `telas/clientes.py`, `produtos.py` e `pedidos.py`: mantêm cada cadastro isolado;
- `database.py`: mantém as operações de acesso ao MySQL.

O projeto usa uma abordagem procedural: as telas são criadas por funções e
não existem classes próprias, herança, `self` ou `super()`. O CustomTkinter
continua usando objetos internamente, pois isso faz parte da biblioteca.

## Manual didático

O passo a passo completo está em
`documentacao/Manual_Projeto_Brecho_CustomTkinter.docx`.

Para gerar novamente o documento após alterar o projeto:

```bash
python -m pip install python-docx
python documentacao/gerar_manual.py
```

`python-docx` é necessário somente para gerar o manual e não para executar o
sistema do brechó.

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
