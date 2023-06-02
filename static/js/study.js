function open_word(){
    var amount= document.getElementById("amount").value;
    url = "http://localhost:8000/word?amount="+amount
    window.location.replace(url);
}