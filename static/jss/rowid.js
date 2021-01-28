function rowid2() {
    var ids = [];
    $('#textboxDiv tr').each(function () {
        ids.push($(this).find('td:first-child input[type="number"]').attr('id'))
        alert(ids)
    })
}
function rowid1() {
        var ids=[];
            $('#textboxDiv input[type="text"]').each(function(){
              ids.push($(this).attr('id'))
                alert(ids)
            })
        }

function rowid() {
        var ids=[];
            $('#tr2').each(function(){
              ids.push($(this).find('input[type="number"]').attr('id'))
                alert(ids)
            })
        }
