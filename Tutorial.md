# Tutorial rápido — Sistema do Brechó

## 1. Programas necessários

Antes de começar, verifique se o computador possui:

* **Python 3**
* **MySQL Server**
* **MySQL Workbench**
* um editor de código, como **Visual Studio Code**

---

# 2. Baixe e extraia o projeto

Extraia a pasta:

`projeto_brecho_uc2`

A estrutura será:

```text
projeto_brecho_uc2/
│
├── app.py
├── config.py
├── database.py
├── requirements.txt
├── README.md
│
└── sql/
    └── schema.sql
```

---

# 3. Crie o banco de dados

Abra o **MySQL Workbench**.

Abra o arquivo:

```text
sql/schema.sql
```

Execute todo o script.

Ele criará:

```text
Banco:
brecho_uc2

Tabelas:
clientes
produtos
pedidos
```

---

# 4. Configure a conexão

Abra:

`config.py`

Localize:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "SUA_SENHA_AQUI",
    "database": "brecho_uc2",
}
```

Substitua:

```text
SUA_SENHA_AQUI
```

pela senha utilizada no seu MySQL.

Exemplo:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "brecho_uc2",
}
```

Salve o arquivo.

---

# 5. Abra o terminal

Abra a pasta do projeto no **Visual Studio Code**.

Depois abra:

**Terminal → Novo Terminal**

Confirme que o terminal está na pasta:

```text
projeto_brecho_uc2
```

---

# 6. Instale as bibliotecas

No terminal, execute:

```bash
pip install -r requirements.txt
```

Serão instalados:

* CustomTkinter;
* conector Python/MySQL.

A instalação precisa ser feita apenas uma vez no computador.

---

# 7. Execute o sistema

No terminal:

```bash
python app.py
```

Se o comando `python` não funcionar no Windows, tente:

```bash
py app.py
```

A tela de login deverá abrir.

---

# 8. Faça o login

Utilize:

```text
Usuário: admin
Senha: 1234
```

Clique em **Entrar**.

> Este login é apenas didático. Usuário e senha estão definidos no próprio programa e não são consultados no banco.

---

# 9. Cadastre um pedido

Na tela seguinte, informe:

```text
Cliente
Tipo: Novo ou VIP
Produto
Quantidade
Preço unitário
Desconto do produto
```

Clique em:

**Calcular**

Confira o subtotal, desconto da cliente e valor final.

Depois clique em:

**Salvar pedido**

O pedido será inserido na tabela `pedidos` do MySQL.

---

# 10. Confira no MySQL

No MySQL Workbench, execute:

```sql
USE brecho_uc2;

SELECT * FROM pedidos;
```

O pedido cadastrado pela aplicação deverá aparecer na tabela.

---

# Fluxo completo

```text
Executar schema.sql
        ↓
Configurar config.py
        ↓
Instalar requirements.txt
        ↓
python app.py
        ↓
LOGIN
        ↓
CADASTRAR PEDIDO
        ↓
CALCULAR
        ↓
SALVAR
        ↓
MYSQL
        ↓
SELECT * FROM pedidos;
```

## Se aparecer erro de conexão

Confira primeiro:

1. se o **MySQL Server está iniciado**;
2. se usuário e senha em `config.py` estão corretos;
3. se o banco `brecho_uc2` foi criado;
4. se `schema.sql` foi executado;
5. se as bibliotecas foram instaladas com `pip install -r requirements.txt`.
