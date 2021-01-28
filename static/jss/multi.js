var textboxvalue;
function textboxid(clickedid) {
    alert(clickedid)
    //alert($(self).attr('id'));
}
function multi(clickedid){
        var rate = document.getElementById(clickedid).value
        var quan = document.getElementById(clickedid+"q").value
        if(document.getElementById(clickedid+"i").value == "select")
        {
            alert("Please select Item")
        }
        else {
            var mult = rate * quan
            document.getElementById(clickedid+"t").value = mult;
        }
}
function receivedone(trp) {
    // alert("Utkarsh")
    // alert(trp)
    var trecived = parseFloat(document.getElementById(trp).value);
    var tpp = parseFloat(document.getElementById("tp").value)
    // alert(trecived)
    // alert(tpp)
    var ts = trecived - tpp;
    if ( ts < 0 ){
        document.getElementById("return").value = 0;
        document.getElementById("due").value = ts;
    }
    else if (ts > 0){
        document.getElementById("due").value = 0;
        document.getElementById("return").value = ts;
    }
}

function totalprice() {
    // alert(clicks)
    var tp = 0;
    var tpp = 0;
    document.getElementById("tp").value = 0;
    var i;
    for (i = 1; i <= clicks; i++){
        tp = parseFloat(document.getElementById("item"+i+"t").value);
        if ( !isNaN(tp) ){
            tpp = tpp + tp;
        }
    }
   // alert(tpp)
    document.getElementById("tp").value = tpp;
}
