//window.onload = initAll;

// function initAll() {
//     alert(window.onload)
//     alert("Utkarsh")
// }

function getvalue() {
    //alert("Utkarsh")
    var itemname = document.getElementById('item2').value;
    var address = document.getElementById('dealeradd').value;
    var quantity = document.getElementById('quantity').value;
    var unitprice = document.getElementById('unitprice').value;
    var datereceived = document.getElementById('datereceived').value;
    var mult = quantity * unitprice
    document.getElementById('totalprice').value = mult;
    // var totalprice = document.getElementById('totalprice').value;
    var totalprice = mult;
     //alert(totalprice)
    allvalues = [itemname, address, quantity, unitprice, datereceived, totalprice];
    //alert(allvalues)
    return allvalues
}

function multip(totalid) {
    // alert(totalid)
    var quantity = document.getElementById(totalid+"q").value;
    var unitprice = document.getElementById(totalid).value;
    if(quantity != null && unitprice!= null)
    {
        var mult = quantity * unitprice
        document.getElementById(totalid+"t").value = mult;
    }

}


function additem() {
    getvalue();
    //alert(allvalues[4] != allvalues[3])
    if( allvalues[0] == "" || allvalues[1] == "" || allvalues[2] == "" || allvalues[3] == "" | allvalues[4] == "" || allvalues[5] == "" ){
    }
    else {
        //alert(allvalues[0])
        var url = '/additem?itemname='+allvalues[0]+'&address='+allvalues[1]+'&quantity='+allvalues[2]+'&unitprice='+allvalues[3]+'&dateitem='+allvalues[4]+'&totalprice='+allvalues[5];
        //alert(url)
        var xhttp = new XMLHttpRequest();
        //alert(xhttp.responseText)
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                signupresponse = xhttp.responseText;
            }
        };
        xhttp.open("GET", url, true);
        xhttp.send();
    }

}