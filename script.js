function loadTasks() {
    fetch("/tasks")
    .then(res => res.json())
    .then(data => {
        let list = document.getElementById("taskList");
        list.innerHTML = "";
        data.forEach(t => {
            list.innerHTML += `
            <li>
                ${t.task}
                <button onclick="deleteTask(${t.id})">❌</button>
            </li>`;
        });
    });
}

function addTask() {
    let task = document.getElementById("taskInput").value;
    fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({task})
    }).then(() => {
        document.getElementById("taskInput").value = "";
        loadTasks();
    });
}

function deleteTask(id) {
    fetch("/delete/" + id, {method: "DELETE"})
    .then(() => loadTasks());
}

loadTasks();
