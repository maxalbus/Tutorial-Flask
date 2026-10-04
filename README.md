# Protótipo Funcional — Gerenciador de Tarefas

Implementação funcional do Gerenciador de Tarefas utilizando Flask.

O sistema permite cadastrar usuários, realizar autenticação, criar e gerenciar tarefas, compartilhar tarefas com outros usuários e controlar o acesso de acordo com o papel de cada usuário.

## Tecnologias

- Python
- Flask
- Jinja2
- Bootstrap 5
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- Flask-Login

## Funcionalidades

### Autenticação

- Cadastro de usuários;
- Senhas armazenadas com hash;
- Login;
- Logout;
- Controle de sessão;
- Redirecionamento de acordo com o papel do usuário.

### Usuários

Existem dois papéis:

**Member**

- Visualiza suas próprias tarefas;
- Visualiza tarefas compartilhadas com ele;
- Cria tarefas;
- Edita e exclui suas próprias tarefas;
- Pode compartilhar suas tarefas.

**Admin**

- Visualiza todas as tarefas;
- Pode criar tarefas;
- Pode editar tarefas;
- Pode excluir tarefas;
- Pode compartilhar tarefas.

O cadastro público cria usuários como `member`. A criação/configuração de um administrador é realizada externamente no banco de dados.

### Tarefas

Cada tarefa possui:

- título;
- descrição;
- status;
- criador;
- usuário com quem foi compartilhada, quando aplicável.

Os status disponíveis são:

- `pending`
- `in progress`
- `completed`

## Rotas principais

| Rota | Função |
|---|---|
| `/` | Redireciona para o login |
| `/login` | Login |
| `/register` | Cadastro |
| `/logout` | Logout |
| `/dashboard` | Painel do usuário |
| `/admin` | Painel administrativo |
| `/add_task` | Criação de tarefa |
| `/edit_task/<id>` | Edição de tarefa |
| `/delete_task/<id>` | Exclusão de tarefa |

## Banco de dados

A aplicação utiliza SQLite e possui duas tabelas principais:

### `users`

Armazena:

- `id`
- `username`
- `password`
- `role`

### `tasks`

Armazena:

- `id`
- `title`
- `description`
- `status`
- `created_by`
- `shared_with`

A tabela de tarefas possui relações com os usuários responsáveis pela criação e pelo compartilhamento.

## Estrutura

```text
.
├── app.py
├── extensions.py
├── models.py
├── requirements.txt
├── REFERENCIA.md
├── instance/
└── templates/
    ├── add_task.html
    ├── admin.html
    ├── base.html
    ├── dashboard.html
    ├── edit_task.html
    ├── login.html
    └── register.html
```

## Como executar

### 1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 2. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

```bash
flask --app app run
```

Depois, acesse:

```text
http://127.0.0.1:5000
```

O banco SQLite é criado automaticamente pela aplicação quando necessário.

## Observação

Esta branch representa a implementação funcional do projeto. O protótipo visual original permanece separado na branch `prototipo-visual`.
