function changeColor() {

    randomInt = Math.floor(Math.random() * 6);
    if (randomInt === 0) {
        document.getElementById("Text").style.color = "red";
    }
    else if (randomInt === 1) {
        document.getElementById("Text").style.color = "blue";
    }
    else if (randomInt === 2) {
        document.getElementById("Text").style.color = "green";
    }
    else if (randomInt === 3) {
        document.getElementById("Text").style.color = "yellow";
    }
    else if (randomInt === 4) {
        document.getElementById("Text").style.color = "cyan";
    }
    else {
        document.getElementById("Text").style.color = "pink";
    }
}

document.getElementById("Change_Color").addEventListener("click", changeColor);