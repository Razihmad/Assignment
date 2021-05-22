function AddInputs()
{
    var total = 0;
    var coll = document.getElementsByClassName("s")
    for ( var i = 0; i<coll.length; i++)
    {
        var ele = coll[i];
        total += parseInt(ele.value);
    }
    document.getElementsByName('total')[0].value = total.toString();
    var t = total/3;
    var x = t.toFixed(2)
    document.getElementsByName('percentage')[0].value =x.toString() ;
}
