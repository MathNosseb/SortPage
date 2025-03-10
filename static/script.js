document.addEventListener("DOMContentLoaded", function() {
    var entry = document.getElementById("input");
    var buttonSend = document.getElementById("send");
    bool selection = 

    buttonSend.addEventListener("click", function() {
        alert("bouton cliqué");
        var entryValue = entry.value;
        console.log(entryValue);
        numberList = entryValue.split(",").map(Number);
        console.log(numberList);
    });
});
