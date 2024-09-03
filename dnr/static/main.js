console.log("JavaScript подключен успешно!");

function allowDrop(event) {
    event.preventDefault();  // Разрешаем сброс элемента
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);  // Сохраняем id перетаскиваемого элемента
}

function drop(event) {
    event.preventDefault();
    let itemID = event.dataTransfer.getData("text");  // Получаем id перетаскиваемого элемента
    let item = document.getElementById(itemID);
    event.target.appendChild(item);  // Добавляем элемент в новую колонку
}

