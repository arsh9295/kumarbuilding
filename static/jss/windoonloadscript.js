function windowsonloadfun() {
    hide()
    textboxeditdisable()
}

function textboxeditdisable() {
    alert("Utkarsh")
    document.getElementById("tp").readOnly = true
}

function hide() {
    document.getElementById("bgblack").style.display = "none";
    document.getElementById("productinput").style.display = "none";
}