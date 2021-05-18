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
    document.getElementsByName('percentage')[0].value = (total/3).toString();
}
