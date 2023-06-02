

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

function load_word(){
    var numArray = [];

    var urlParams = new URLSearchParams(window.location.search);
    var amount = urlParams.get('amount');
    var data = localStorage.getItem("data");
    var target = document.getElementsByClassName("test_box")[0];
    console.log(target)

    var words = JSON.parse(data);

    var jsonArray = [
    ];
    

    var result = [];


    for (var i = 0; i < 600; i++) {
        numArray.push(i);
    }


    for (var j = 0; j < amount; j++) {
        var randomIndex = Math.floor(Math.random() * numArray.length);
        var randomNumber = numArray[randomIndex];

        
        

        // 중복된 값 제거
        numArray.splice(randomIndex, 1);

        result.push(randomNumber);

    
        target.innerHTML +=`
        <div class="word">
            <button class = "fa-solid fa-plus" onclick="add_voc(this)"></button>
            <div class="name">${words[randomNumber].name}</div>
            <div class="mean">${words[randomNumber].mean}</div>
        </div>
        `;

        jsonArray.push({"name": words[randomNumber].name, "mean": words[randomNumber].mean});
    }

    localStorage.removeItem("test");
    localStorage.setItem("test", JSON.stringify(jsonArray));
}

load_word();

function add_voc(e){
    document.getElementById("modal").display = "block";
}

