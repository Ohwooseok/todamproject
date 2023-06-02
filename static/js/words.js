var button = document.getElementsByClassName("test_button")[0];
function hide(){
    const means = document.getElementsByClassName('mean');
    const meansArray = Array.from(means);
    meansArray.forEach(mean => {
        mean.style.display = "none";
    })

    button.style.backgroundColor = "rgb(228, 53, 18)";
    button.removeAttribute("onclick");
    button.setAttribute("onclick", "show()");
}

function show(){
    const means = document.getElementsByClassName('mean');
    const meansArray = Array.from(means);
    meansArray.forEach(mean => {
        mean.style.display = "block";
    })

    button.style.backgroundColor = "rgb(45, 218, 71)";
    button.removeAttribute("onclick");
    button.setAttribute("onclick", "hide()");
}