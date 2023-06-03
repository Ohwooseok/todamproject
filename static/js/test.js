localStorage.setItem("score", 0)
function getRandomUniqueInt(min, max, count) {
    var numArray = [];
  
    // 범위 내의 모든 정수를 배열에 추가
    for (var i = min; i <= max; i++) {
      numArray.push(i);
    }
  
    var result = [];
  
    // 지정된 개수만큼 랜덤한 정수 추출
    for (var j = 0; j < count; j++) {
      var randomIndex = Math.floor(Math.random() * numArray.length);
      var randomNumber = numArray[randomIndex];
  
      // 중복된 값 제거
      numArray.splice(randomIndex, 1);
  
      result.push(randomNumber);
    }
  
    return result;
  }

function load_word(){
    var words = JSON.parse(localStorage.getItem("data"));
    var data = JSON.parse(localStorage.getItem("test"));
    var target = document.getElementsByClassName("test_box")[0];

    nums = [];
    nums = getRandomUniqueInt(0, data.length-1, data.length)
    console.log(nums);


    for (var i =0; i<nums.length; i++){
        var randomIndex1 = Math.floor(Math.random() * words.length);
        var randomIndex2 = Math.floor(Math.random() * words.length);
        answers = [];
        answers.push(data[nums[i]].mean);
        answers.push(words[randomIndex1].mean);
        answers.push(words[randomIndex2].mean);

        nums1 = getRandomUniqueInt(0, 2, 3);

        answer_total = [];
        for (var j =0; j<3; j++){
            answer_total.push(answers[nums1[j]]);
        }
        target.innerHTML +=`
        <div class="word">
            <div class="name">${data[nums[i]].name}</div>
            <div class="test_answer">
                <button class="mean" onclick="check(this)">${answer_total[0]}</button>
                <button class="mean" onclick="check(this)">${answer_total[1]}</button>
                <button class="mean" onclick="check(this)">${answer_total[2]}</button>
                <button class="mean" onclick="check(this)">모르겠음</button>    
            </div>
        </div>
        `;
    }

        
}

load_word();

function check(e){
    var word = e.parentNode.parentNode.getElementsByClassName('name')[0].innerText;
    var answer = e.innerText;

    for(var i = 0; i<data.length; i++){
        var score = parseInt(localStorage.getItem("score"))
        if(data[i].name == word){
            if(data[i].mean == answer){
                e.style.backgroundColor = "green";
                localStorage.setItem("score", score+1)
            }else{
                e.style.backgroundColor = "red";
            }
        }
    }
    var buttons = e.parentNode.getElementsByClassName("mean");
    for(var i = 0; i <4; i++){
        buttons[i].disabled = true;
    }

    document.getElementById("score").innerText = localStorage.getItem("score");

}

