// window.onload = function() {
//  alert("let's go!");
// }

function hide() {
    document.getElementById("bgblack").style.display = "none";
    document.getElementById("productinput").style.display = "none";
}

function show() {
    document.getElementById("bgblack").style.display = "block";
    document.getElementById("productinput").style.display = "block";
}


function textboxeditdisable() {
    // alert("Utkarsh")
    document.getElementById("tp").readOnly = true
    document.getElementById("due").readOnly = true
    document.getElementById("return").readOnly = true
    // document.getElementById("item1t").readOnly = true
    var i;
    for( i=1; i<=clicks; i++){
        // alert(i)
        // document.getElementById("item"+i+"t").value = 12
        document.getElementById("item"+i+"t").readOnly = true
    }
}