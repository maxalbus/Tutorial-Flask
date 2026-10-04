# Referência do projeto

## Objetivo

Implementar, de forma incremental e didática, um gerenciador de tarefas para uma equipe, reproduzindo o funcionamento do tutorial acadêmico. A prioridade é manter a solução simples e próxima do tutorial, sem adicionar arquitetura ou abstrações desnecessárias.

## Tecnologias

- Python
- Flask
- SQLite 3
- SQLAlchemy
- Flask-Login
- Jinja2
- Bootstrap

## Organização prevista

- `app.py`: aplicação e lógica principal, incluindo configuração, autenticação e rotas.
- `models.py`: modelos de usuário e tarefa.
- `extensions.py`: extensões usadas pela aplicação.
- `templates/`: templates Jinja2.

Templates inicialmente previstos: `base.html`, `login.html`, `register.html`, `dashboard.html`, `admin.html` e `add_task.html`. Outros arquivos só serão incluídos se uma necessidade concreta surgir ou se o tutorial exigir.

Não criar inicialmente `config.py`, `forms.py`, `routes.py`, blueprints, services, repositories ou outras camadas.

## Dados e permissões

Existem dois papéis de usuário: `admin` e `member`.

Um usuário possui `id`, `username`, senha armazenada como hash e `role` (`admin` ou `member`).

Uma tarefa possui `id`, `title`, `description`, `status`, usuário criador (`created_by`) e usuário com quem foi compartilhada (`shared_with`). Um usuário pode criar várias tarefas e receber várias tarefas compartilhadas.

- Admin: pode visualizar todas as tarefas, criar, editar, excluir e compartilhar tarefas.
- Member: pode visualizar as tarefas que criou e as compartilhadas com ele; pode criar tarefas e editar, excluir ou compartilhar somente tarefas próprias.
- Um member não pode editar nem excluir tarefas criadas por outra pessoa.

## Autenticação e navegação

1. A rota `/` apresenta a entrada/login.
2. O usuário pode acessar o cadastro.
3. O cadastro armazena a senha usando hash.
4. O login verifica as credenciais e Flask-Login mantém a sessão autenticada.
5. Após autenticar, admin segue para o painel administrativo e member para o dashboard.
6. O logout encerra a sessão e retorna ao login.

Funcionalidades previstas: registro, login, dashboard de member, painel de admin, criação, edição e exclusão de tarefas, compartilhamento durante a criação ou gerenciamento da tarefa e logout.

## Implementação incremental

Ordem de trabalho prevista:

1. Estrutura do projeto.
2. Extensões.
3. Modelos.
4. Configuração da aplicação.
5. Autenticação.
6. Dashboard de member.
7. Painel de admin.
8. Criação de tarefas.
9. Compartilhamento.
10. Edição.
11. Exclusão.
12. Templates.
13. Bootstrap e estilo.
14. Testes.

## Regra de autorização para mudanças

Antes de cada etapa de implementação, explicar o que será feito e quais arquivos serão modificados, e aguardar autorização. Não implementar várias etapas de uma vez, nem fazer refatorações ou mudanças arquiteturais por iniciativa própria. Criar um arquivo novo somente quando houver necessidade concreta ou exigência do tutorial.