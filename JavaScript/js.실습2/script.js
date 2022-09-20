const numbersDiv = document.querySelector(".numbers");
//numbers 는 클래스 이므로 .numbers
const drawButton = document.querySelector("#draw");
const resetButton = document.querySelector("#reset");
//draw 와 reset 은 id 이므로 앞에 #을 넣어줍니다.

const lottoNumbers = [];
//로또 번호를 담을 배열을 생성합니다.
const colors = ["red","orange","yellow","green","blue","purple","clear","pink"];
//로또 볼에 색을 더해줄수있는 배열을 생성합니다.


function paintNumber(number){
  const i = lottoNumbers.length;
  setTimeout(function(){
    const eachNumDiv = document.createElement("div");
    eachNumDiv.classList.add('eachnum');
    eachNumDiv.style.backgroundColor = colors[i-1];
    //색상을 입혀줍니다.
    eachNumDiv.textContent = number;
    numbersDiv.appendChild(eachNumDiv)
  });
}
drawButton.addEventListener("click",function(){
  //  console.log("!"); //화면에 잘나오는지 확인하기.
  while(lottoNumbers.length < 8){
      var num=Math.floor(Math.random()*45)+1;
      if(lottoNumbers.indexOf(num) === -1){ 
        //중복되는 숫자가 없을시에 값을 push 해줍니다.
        if(lottoNumbers.length==6){
          num = "+"; //보너스ball 앞에 넣어준다.
        }
        lottoNumbers.push(num)
        paintNumber(num);
      } 
  }
  // console.log(lottoNumbers); //colsole 에서 확인하기.
})
resetButton.addEventListener("click",function(){ 
  lottoNumbers.splice(0,8);
  numbersDiv.innerHTML = "";
  //reset 버튼을 누르면 numbers 안에 값을 비워준다.
  history.go(0);
  /*lotto ball 이 생성되는 중간에 reset 버튼을 누르면 그뒤에 담겨있던 나머지 볼들이 계속나와서
  history.go 를 추가해주었다 페이시 새로고침이되서 처음값으로 돌아간다.*/
})