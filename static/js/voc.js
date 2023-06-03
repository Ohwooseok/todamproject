function add(){
    var target = document.getElementsByClassName('voc_list')[0];

    var htmlStr =`
    <input type="text" class="voc new" placeholder="새 단어장 이름 입력" >
            <button class="add_comp fa-solid fa-check" onclick="add_comp(this)"></button>
            <button class="add_comp fa-solid fa-xmark" onclick="add_cancle(this)"></button>
    `;

    target.innerHTML += htmlStr;

}

function add_comp(e){
    var target = document.getElementsByClassName('voc_list')[0];
    var name = e.parentNode.getElementsByTagName("input")[0].value;
    localStorage.setItem("voc_"+name, "")

    var parent = e.parentNode;
    var remove = e.parentNode.getElementsByClassName("new")[0];
    var remove1 = e.parentNode.getElementsByClassName("fa-check")[0];
    var remove2 = e.parentNode.getElementsByClassName("fa-xmark")[0];
    parent.removeChild(remove);
    parent.removeChild(remove1);
    parent.removeChild(remove2);

    var htmlStr=`
    <div class="voc">${name}<button class="fa-solid fa-trash" onclick="delete_voc('${name}')"></div>
    `;

    target.innerHTML += htmlStr;

}

function add_cancle(e){

    var parent = e.parentNode;
    var remove = e.parentNode.getElementsByClassName("new")[0];
    var remove1 = e.parentNode.getElementsByClassName("fa-check")[0];
    var remove2 = e.parentNode.getElementsByClassName("fa-xmark")[0];
    parent.removeChild(remove);
    parent.removeChild(remove1);
    parent.removeChild(remove2);
}

function load_voc(){
    document.getElementsByClassName("voc_list")[0].innerHTML = "";
    var target = document.getElementsByClassName('voc_list')[0];
    var keys = Object.keys(localStorage).filter(function(key) {
        return key.startsWith('voc_');
      });

    for (var i = 0; i< keys.length; i++){
        var htmlStr=`
        <div class="voc">${keys[i].slice(4)}<button class="fa-solid fa-trash" onclick="delete_voc('${keys[i].slice(4)}')"></div>
        `;

        target.innerHTML += htmlStr;
    }
}

load_voc();

function delete_voc(name){
    localStorage.removeItem("voc_"+name);
    load_voc();
}