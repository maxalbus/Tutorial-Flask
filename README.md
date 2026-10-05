# Tutorial Flask — Gerenciador de Tarefas

O projeto possui duas implementações separadas, desenvolvidas com objetivos diferentes:

- **Protótipo visual:** interface inicial desenvolvida com HTML, CSS e JavaScript, voltada à apresentação visual e à experiência de uso.
- **Protótipo funcional:** implementação completa do sistema utilizando Flask, SQLite, SQLAlchemy e Flask-Login, com autenticação, usuários, tarefas e controle de permissões.

## Branches

### `prototipo-visual`

Contém o protótipo visual do projeto.

Tecnologias principais:

- HTML
- CSS
- JavaScript
- Flask

O protótipo utiliza JavaScript para simular as interações e não possui persistência de dados em banco.

### `prototipo-funcional`

Contém a implementação funcional do gerenciador de tarefas.

Tecnologias principais:

- Python
- Flask
- Jinja2
- Bootstrap
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- Flask-Login

A implementação funcional possui autenticação, diferentes papéis de usuário, criação e gerenciamento de tarefas, compartilhamento e controle de permissões.

## Organização

As duas implementações permanecem em branches separadas para evitar que uma substitua ou descaracterize a outra.

```text
Tutorial-Flask
│
├── main
│
├── prototipo-visual
│   └── Protótipo de interface
│
└── prototipo-funcional
    └── Sistema funcional
```

## Execução

Cada branch possui seu próprio README com as instruções específicas para execução.

https://www.figma.com/design/58ThVNmyTFwqVpSCAr4gIx/Sem-t%C3%ADtulo?node-id=0-1&t=EBlmmNZ8CwoXHNIZ-1