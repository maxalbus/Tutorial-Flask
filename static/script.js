function entrar(event) {
    event.preventDefault();

    const mensagem = document.getElementById("mensagem");
    mensagem.textContent = "Login demonstrativo realizado!";

    setTimeout(() => {
        window.location.href = "/tarefas";
    }, 800);
}

let tarefas = [];

function adicionarTarefa() {
    const campo = document.getElementById("novaTarefa");
    const texto = campo.value.trim();

    if (texto === "") {
        return;
    }

    tarefas.push({
        texto: texto,
        concluida: false
    });

    campo.value = "";
    mostrarTarefas();
}

function concluirTarefa(indice) {
    tarefas[indice].concluida = !tarefas[indice].concluida;
    mostrarTarefas();
}

function excluirTarefa(indice) {
    tarefas.splice(indice, 1);
    mostrarTarefas();
}

function mostrarTarefas() {
    const lista = document.getElementById("listaTarefas");
    const vazio = document.getElementById("vazio");
    const contador = document.getElementById("contador");

    lista.innerHTML = "";

    tarefas.forEach((tarefa, indice) => {
        const item = document.createElement("li");
        item.className = tarefa.concluida ? "tarefa concluida" : "tarefa";

        item.innerHTML = `
            <input type="checkbox"
                   ${tarefa.concluida ? "checked" : ""}
                   onchange="concluirTarefa(${indice})">
            <span>${tarefa.texto}</span>
            <button class="excluir" onclick="excluirTarefa(${indice})">Excluir</button>
        `;

        lista.appendChild(item);
    });

    vazio.style.display = tarefas.length === 0 ? "block" : "none";
    contador.textContent = tarefas.length + (tarefas.length === 1 ? " tarefa" : " tarefas");
}
