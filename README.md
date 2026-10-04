# Protótipo Visual — Gerenciador de Tarefas

Protótipo inicial do Gerenciador de Tarefas, desenvolvido para representar a interface e o fluxo visual da aplicação.

Esta versão tem foco na **interface e experiência de uso**. As interações são simuladas com JavaScript e os dados das tarefas permanecem apenas durante a execução da página.

## Tecnologias

- HTML5
- CSS3
- JavaScript
- Flask

## Funcionalidades

O protótipo apresenta:

- Tela inicial;
- Tela de login;
- Tela de tarefas;
- Criação de tarefas;
- Conclusão de tarefas;
- Exclusão de tarefas;
- Contador de tarefas;
- Layout responsivo.

O login é demonstrativo e não utiliza autenticação real.

As tarefas são armazenadas em memória no JavaScript e não são persistidas em banco de dados.

## Estrutura

```text
.
├── app.py
├── requirements.txt
├── static/
│   ├── script.js
│   └── style.css
└── templates/
    ├── index.html
    ├── login.html
    └── tarefas.html
```

## Como executar

### 1. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 2. Ativar o ambiente virtual

Linux/macOS:

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

## Observação

Esta branch representa o protótipo visual do projeto. A implementação com banco de dados, autenticação real e controle de permissões está disponível na branch `prototipo-funcional`.
