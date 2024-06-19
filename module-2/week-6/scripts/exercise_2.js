function showData() {
    let board = document.getElementById("result");
    let text = document.getElementById("Content");
    let information = document.createElement("p");

    information.id = "NewElement";
    information.textContent = text.value;

    let NewElement = document.getElementById("NewElement");
    if (NewElement){
        board.replaceChild(information, NewElement);
    } else {
        board.appendChild(information);
    }
    text.value = "";
}