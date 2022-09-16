#### 변수와 식별자

- 식별자: (identifier)변수를 구분할 수 있는 변수명 반드시 문자, $ 또는 _ 로 시작
  - 대소문자 구분, 클래스 외에는 모두 소문자 시작.
  - 예약어(for,if,function 등 함수?) 불가능



- 선언,할당,초기화

- 선언(Declaration)

  - 변수를 생성하는 행위 또는 시점

- 할당(Assignment)

  - 선언된 변수에 값을 저장하는 행위 또는 시점

- 초기화(Initialization)

  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

- ``` javascript
  let foo //  Declaration
  console.log(foo)  //  undefined
  
  foo = ll // Assignment
  console.log(foo) // ll
  
  let bar = 0 // Declaration + Assignment
  console.log(bar) // 0
  ```

- 

#### let,const vs var

- let,const

  - ``` javascript
    let number = 10 // 선언 및 초기값 할당.
    number = 10  // 재할당
    
    console.log(number) // 10 // let = 재할당이 가능하다.
    
    const number = 10 // 선언 및 초기값 할당.
    number = 10 // TypeError, const = 재할당이 불가능.
    ```

  - ``` javascript
    let number = 10 // 
    let number = 50 // syntaxError , 재선언은 불가능 하다.
    
    const number = 10 
    const number = 50  // SysntaxError , 재선언 불가능 2
    ```

  - 블록스코프

    - if,for 함수 등의 중괄호 내부를 가리킴

    - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

    - ``` javascript
      let x = 1
      if (x===1){
          let x = 2
          console.log(x)  // 2 // 블록스코프 내에서만.
      }
      console.log(x)  // 1 // 접근이 불가
      ```

    - 

- var

  - var로 선언한 변수는 재선언 및 재할당 모두가능

  - ES6이전에 변수를 선언할때 사용되던 키워드

  - 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 기능

    - 따라서 ES6 이후부터는 var 대신 const와 let 을 사용하는 것을 권장

    - ``` javascript
      var number = 10 //
      var number = 50 // 재할당
      
      console.log(number) // 50 // 재선언 및 재할당이 모두 가능.
      ```

  - 함수 스코프(function scope)

    - 함수의 중괄호 내부를 가리킴

    - 함수 스코프를 가지는 변수는 함수 밖에서 접근 불가능

    - ``` javascript
      function foo(){
          var x = 5
          console.log(x)  // 5
      }
      // ReferenceError: x 가 위에서 정의되지않음.(선언이나 할당이 되지않았다.)
      console.log(x)
      ```

    - 

#### 호이스팅

- 호이스팅

  - 변수를 선언 이전에 참조할 수 있는 현상

  - 변수 선언 이전의 위치에서 접근 시 undefined를 반환

  - ``` javascript
    console.log(username)  // undefined
    var username = '길동홍'
    
    console.log(email)  // uncaught ReferenceError
    let email = 'asd@asd.com'
    
    console.log(age) // uncaught ReferenceError
    const age = 50
    ```

  - 

- 자바스크립트는 모든 선언을 호이스팅한다.

- 즉,  var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않는다.

- ![image-20220916095216792](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916095216792.png)

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시타입과 참조타입으로 분류됨
- ![image-20220916141558859](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916141558859.png)

- 원시타입 (Primitive type)

  - 객체가 아닌 기본 타입

  - 변수에 해당 타입의 값이 담김

  - 다른 변수에 복사 할때 값이 복사됨.

  - ``` javascript
    let message = '안녕하세요' //
    
    let greeting = message  // greeting 변수에 message 복사
    console.log(greeting)  // 안녕하세요
    
    message = 'Helo,world'  // 재할당
    console.log(greeting)  // 안녕하세요 가 다시출력.
    
    //=> 원시타입은 실제 해당 타입의 값을 변수에 저장.
    ```

- 참조타입(Reference type)

  - 객체 타입의 자료형

  - 변수에 해당 객체의 참조 값이 담김

  - 다른 변수에 복사할때 참조값이 복사됨

  - ``` javascript
    const message = ['안녕']
    
    const greeting = message
    console.log(greeting) // 안녕
    
    message[0] = 'helo'
    console.log(greeting)  // ['helo'] 출력
    
    //=> 참조 타입은 해당객체를 참조할 수 있는 참조 값을 저장.
    ```

  - 

- 숫자타입

  - 정수, 실수 구분 없는 하나의 숫자타입.

  - 부동소수점 형식을 따름.

  - NaN(NotANumber)

    - 계산불가능한 값. 타입이 다른데 식을 대입하였을때 반환되는 값

  - ``` javascript
    const a = 2.998e8
    const e = Infinity
    const d = -Infinity
    const g = NaN
    ```

- 문자열타입

  - 텍스트 데이터를 나타내는 타입

  - 16비트 유니코드 문자의 집합

  - 작은 따옴표 또는 큰 따옴표 모두 가능

  - 템플릿 리터럴

    - ES6 부터 지원
    - 따옴표 대신 Backtick(`) 으로 표현
    - ${expression}로 표현식 삽입 가능

  - ```javascript
    const fname = 'B'
    const lname = 'e'
    const full = `${fname}${lname}`
    
    console.log(full)  // Be
    ```

- undefined

  - 변수의 값이 없음을 나타내는 데이터 타입

  - 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined 가 할당된다.

  - ``` javascript
    let fName
    console.log(fName) // undefined
    ```

- null

  - 변수의 값이 없음을 의도적으로 표현할때 사용하는 데이터타입

  - null 타입과 typeof 연산자

    - typeof연산자:자료형평가를위한연산자

    - null타입은ECMA명세의원시타입의정의에따라원시타입에속하지만,typeof 연산자의 결과는 객체로 표현됨

    - ``` javascript
      let firstName = null
      console.log(firstname)
      
      typeof null // object ?? 
      ```

- boolean타입

  - 논리적 참 또는 거짓

  - 조건문이나 반복문에서 사용

  - ``` javascript
    let i = true
    console.log(i) // true
    
    i = false
    console.log(i) // false
    ```

- 자동형변환정리

- ![image-20220916143337983](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916143337983.png)

#### 할당연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

- 다양한 연산에 대한 단축 연산자 지원

- increment,decrement

  - ++ : 피연산자의 값을 1 증가

  - -- :피연산자의 값을 1 감소

  - +=, -=, *=, /=, 파이썬과 같음.

  - ``` javascript
    let x = 0
    x++
    console.log(x) // 1
    
    x--
    console.log(x) // 0
    ```

- 비교연산자

  - 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자

  - 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

    - 알파벳끼리 비교할경우
      - 소문자가 대문자보다 크며 순서상 후순위가 더 크다.

  - ```javascript
    const one = 1
    const two = 100
    console.log(one < two) // true
    
    const one = 'a'
    const two = 'z'
    console.log(one>two) // false
    ```

- 동등비교연산자(==)

  - 두 피연산자가 같은값인지 비교 후 boolean으로 반환

  - 암묵적 타입변환을 통해 일치시킨 후 비교.

  - 모두 객체일 경우 같은 객체를 바라보는지 판별

  - 특별한 경우를 제외하고 사용 X

  - ```javascript
    const a = 1004
    const b = '1004'
    console.log(a==b) // true
    
    const c = 1
    const d = true
    console.log(c==d)  // true
    
    console.log(a+b) // 10041004
    console.log(c+d) // 2  
    ```

- 일치 비교 연산자(===)

  - 두 피 연산자가 같은 값으로 평가되는지 비교 후 boolean값을 반환

  - 엄격한 비교가 이뤄지며 암묵적 타입 변환 발생하지 않는다.

  - ```javascript
    const a = 1004
    const b = '1004'
    console.log(a===b) // false
    
    const c = 1
    const d = true
    console.log(c===d)  // false
    ```

- 논리 연산자

  - 세가지 논리 연산자로 구성

    - and 연산은 && 연산자 이용
    - or 연산은 || 연산자 이용
    - not 연산은 ! 연산자 이용

  - ``` javascript
    console.log(true && false) // false
    console.log(true && true) // true
    console.log(1 && 0) // 0
    console.log(4 && 7) // 7
    console.log('' && 5) // ''
    
    console.log(true || false) // true
    console.log(false || false) // false
    console.log(1 || 0) // 0
    console.log(4 || 7) // 4
    console.log('' || 5) // 5
    
    console.log(!true) // false
    console.log(!'bonjour') // false
    ```

- 삼항연산자

  - 세 개의 피 연산자를 사용하여 조건에 따라 값을 반환하는 연산자

  - 가장 왼쪽의 조건식이 참이면 콜론 앞의 값을 사용하고 그렇지 않으면 콜론 뒤의 값을 사용

  - 삼항 연산자의 결과값이기 때문에 변수에 할당가능

  - 한줄에 표기하는것을 권장

  - ``` javascript
    console.log(true ? 1:2) // 1
    console.log(false ? 1:2) // 2
    
    const result = Math.PI > 4 ? 'yes' : 'no'
    console.log(result) // no
    ```

#### 조건문

- 조건문의 종류와 특징

  - if statement

    - 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

  - if , else if, else

    - 조건은 소괄호 안에

    - 실행할 코드는 중괄호 안에

    - 블록스코프생성

    - ``` javascript
      const nation = 'korea'
      
      if(nation === 'korea'){
          console.log('안녕하세요')
      } else if (nation === 'france'){
          console.log('봉주르')
      } else {
          console.log('hello')
      }
      ```

  - switch statement

    - 조건 표현식의 결과값이 어느 값에 해당하는지.
      - 주로 특정변수의 값에 따라 조건을 분기할때 활용
      - 조건이 많아질 경우 if문보다 가독성이 UP
    - 표현식의 결과값을 이용한 조건문
    - 표현식의 결과값과 case 문의 오른쪽 값을 비교
    - break 및 default 문은 선택적으로 사용 가능
    - break문을 만나거나 default 문을 실행할때까지 다음 조건문 실행

  - ``` javascript
    const expr = 'strawberry';
    switch (expr) {
      case 'Oranges':
        console.log('Oranges are $0.59 a pound.');
        break;
      case 'Mangoes':
      case 'Papayas':
        console.log('Mangoes and papayas are $2.79 a pound.');
        // expected output: "Mangoes and papayas are $2.79 a pound."
        break;
      default:
        console.log(`Sorry, we are out of ${expr}.`);
    }
    ```

  - ``` javascript
    const one = 5;
    const two = 10;
    let operator = '+';
    
    if (operator === '+'){
        console.log(one+two);
    } else if (operator === '-'){
        console.log(one-two);
    } else if (operator === '*'){
        console.log(one*two);
    } else if (operator === '/'){
        console.log(one/two);
    } else {
        console.log('연산자넣으시오.');
    }
    ```

  - ``` javascript
    const one = 5;
    const two = 10;
    let operator = '+';
    
    switch(operator) {
        case '+': {
            console.log(one+two);
            break;
        }
        case '-': {
            console.log(one-two);
            break;
        }
        case '*': {
            console.log(one*two);
            break;
        }
        case '/': {
            console.log(one/two);
            break;
        }
        default: {
            console.log('연산자넣으시오.');
        }
    }
    ```

#### 반복문

- while

  - 조건문이 true인 동안 반복시행

  - 조건은 소괄호 안

  - 실행할 코드는 중괄호

  - 블록스코프 생성

  - ``` javascript
    let i = 0
    
    while (i < 6){ // i가 6보다 작을때만
        console.log(i) // 0,1,2,3,4,5
        i += 1
    }
    ```

- for

  - 세미콜론으로 구분되는 세 부분으로 구성

  - initialization

    - 최초 반복문 진입 시 1회만 실행되는 부분

  - condition

    - 매 반복 시행 전 평가되는 부분

  - expression

    - 매 반복 시행 이후 평가되는 부분

  - 블록스코프 생성

  - ```javascript
    for(let i = 0; i < 6; i++){ // i=0이고 i가 6보다 작다면 1씩 더하라.
        console.log(i) // 0,1,2,3,4,5
    }
    ```

- for...in

  - 객체의 속성(key)들을 순회할 때 사용

  - 배열도 순회 가능하지만 권장 X

  - 실행할 코드는 중괄호 안에 작성

  - 블록스코프 생성

  - ```javascript
    const capitals = {
        korea: 'seoul',
        france: 'paris',
        usa: 'washington'
    }
    for (let capital in capitals){
        console.log(capital)// key값: korea,france,usa
        console.log(capitals[capital]) // value: seoul,paris,washington 
    }
    ```

- for...of

  - 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용

  - 실행할 코드는 중괄호 안에 작성

  - 블록 스코프 생성

  - ``` javascript
    const fruits = ['딸기', '바나나', '메론']
    
    for (let fruit of fruits){
        fruit = fruit + '!'
        console.log(fruit)
    }
    ```

- for...in vs for..of

  - ```javascript
    //array
    const fruits = ['strawberry','banana','melon']
    
    for (let fruit in fruits){
        console.log(fruit) /// 0,1,2
    }
    // object
    const capitals={
        korea:'seoul'
        france:'paris'
        japan:'tokyo'
    }
    for (let capital in capitals){
        console.log(capital) // korea,france,usa
    }
    ```

    

  - ```javascript
    //array
    const fruits = ['strawberry','banana','melon']
    
    for(let fruit of fruits){
        console.log(fruit) // strawberry,banana,melon
    }
    // object
    const capitals={
        korea:'seoul'
        france:'paris'
        japan:'tokyo'
    }
    
    for(let capital of capitals){
        console.log(capital)
        // TypeError:~~
    }
    ```

#### 함수

- 참조 타입 중 하나로써 function 타입에 속함

- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분

  - 함수선언식
  - 함수표현식

- JavaScript의 함수는 일급객체에 해당

  - 일급객체 : 다음의조건들을 만족하는 객체를 의미함.
    - 변수에 할당가능
    - 함수의 매개변수로 전달가능
    - 함수의 반환 값으로 사용가능

- 함수선언식

  - 함수의 이름과함께 정의하는방식

  - 3가지 부분으로 구성

    - 함수의이름

    - 매개변수

    - 함수body

    - ``` javascript
      function add(num1,num2){
          return num1+num2
      }
      add(1,2)
      ```

- 함수표현식

  - 함수를 표현식 내에서 정의하는 방식

    - 표현식 : 어떤 하나의 값으로 결정되는 코드의 단위

  - 함수의 이름을 생략하고 익명 함수로 정의가능

    - 익명 함수 : 이름이 없는 함수
    - 익명 함수는 함수표현식에서만가능

  - 3가지 부분으로 구성

    - 함수의이름(생략가능)

    - 매개변수(args)

    - 몸통(중괄호 내부)

    - ```javascript
      const add = function(num1,num2){
          return num1 + num2
      }
      add(1,2)
      ```

- 기본인자

  - 인자 작성시 '=' 문자 뒤 기본 인자 선언 가능

  - ```javascript
    const greeting = function (name = 'Anonymous') {
        return `Hi ${name}`
    }
    greeting()
    ```

- 매개변수와 인자의 개수 불일치 허용

  - 매개변수가 인자의 개수보다 많을 경우

  - ```javascript
    const noArgs = function() {
        return 0
    }
    
    noArgs(1,2,3) // 0
    
    const twoArgs = function (arg1,arg2) {
        return [arg1,arg2]
    }
    
    twoArgs(1,2,3) // [1,2]
    ```

  - 매개변수보다 인자의 개수가 적을 경우

  - ```javascript
    const threeArgs = function(arg1,arg2,arg3){
        return [arg1,arg2,arg3]
    }
    threeArgs()
    threeArgs(1)
    threeArgs(1,2)
    ```

- Rest parameter

  - restparameter(...)를 사용하면 함수가 정해지지않은수의 매개변수를 배열로 받음

    - 만약 ~로 처리한 매개변수에 인자가 넘어오지않을경우에는 빈배열로 처리.

    - ```javascript
      const restOpr = function (arg1,arg2, ...restArgs){
          return[arg1,arg2,restArgs]
      }
      
      restArgs(1,2,3,4,5) // [1,2,[3,4,5]]
      restArgs(1,2) // [1,2,[]]
      ```

- spread operator

  - spread operator 를 사용하면 배열 인자를 전개하여 전달 가능.

  - ```javascript
    const spreadOpr = function (arg1,arg2,arg3) {
        return arg1 + arg2 + arg3
    }
    
    const numbers = [1,2,3]
    spreadOpr(...numbers) // 6
    ```

- 함수 선언식과 표현식 비교 정리

  - ![image-20220916161016524](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916161016524.png)

- 함수의 타입

  - 선언식 함수와 표현식 함수 모두 타입은 function

  - ```javascript
    const add = function(args){
        //'do it something'
    }
    
    function sub(args){
        //do it something
    }
    console.log(typeof add) // function
    console.log(typeof sub) // function
    ```

- 호이스팅 - 함수선언식

  - 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 호이스팅 발생

  - 함수 호출 이후에 선언해도 동작!

    - ```javascript
      add(2,7)
      
      function add (num1,num2){
          return num1 + num2
      }
      ```

- 호이스팅 - 함수 표현식

  - 함수표현식으로 선언한 함수는 함수 정의 전 호출 시 에러발생!

  - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름.

  - ```javascript
    sub(7,2) //Error
    
    const sub = function(num1,num2){
        return num1 - num2
    }
    ```

- 화살표 함수

  - 함수를 비교적 간결하게 정의.

  - function 키워드 생략 가능

  - 함수의 매개변수가 단 하나뿐이라면 소괄호도 생략가능

  - 함수 body에 표현식이 하나라면 중괄호와 return도 생략가능

  - ```javascript
    const arrow1 = function(name){
        return `hello, ${name}`
    }
    // function 생략
    const arrow2 = (name) => {return `hello, ${name}`}
    // 소괄호생략
    const arrow3 = name => {return `hello, ${name}`}
    //표현식 달랑 하나일때 중괄호와 return 생략
    const arrow4 = name => `hello, ${name}`
    ```

- 문자열 관련 주요 메서드

  - ![image-20220916162002537](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916162002537.png)

  - string.includes(value)

    - 문자열에  value가 존재하는지 판별 후 참 또는 거짓반환

    - ```javascript
      const str = 'saturday night'
      
      str.includes('saturday') // true
      str.includes('morning') // false
      ```

  - string.split(value)

    - value가 없을 경우, 기존 문자열을 배열에 담아 반환

    - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환

    - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환

    - ```javascript
      const str = 'a cup'
      
      str.split()
      str.split('')
      str.split(' ')
      ```

  - string.replace(from,to)

    - 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환

  - string.replaceAll(from,to)

    - 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환

  - ```javascript
    const str = 'a b c d'
    
    str.replace(' ', '-')   // 'a-b c d'
    str.replaceAll(' '.'-')  // 'a-b-c-d'
    ```

  - string.trim()

    - 문자열 시작과 끝의 모든 공백문자(스페이스,탭,엔터 등)을 제거한 문자열 반환

  - string.trimStart()

    - 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)을 제거한 문자열 반환

  -  string.trimEnd()

    - 문자열 끝의 공백문자(스페이스,탭,엔터 등)을 제거한 문자열 반환

  - ```javascript
    const str = '     hello    '
    
    str.trim()  // 'hello'
    str.trimStart()   // 'hello    '
    str.trimEnd()  // '    hello'
    ```

- 배열의 정의와 특징

  - 키와 속성들을 담고 있는 참조 타입의 객체

  - 순서를 보장하는 특징이 있다.

  - 주로 대괄호를 이용하여 생성하고 , 0을 포함한 양의 정수 인덱스로 특정값에 접근 가능

  - 배열의 길이는 array.length 형태로 접근 가능

    - 배열의 마지막원소는 array.length -1 로 접근

  - ``` javascript
    const numbers = [1,2,3,4,5]
    
    console.log(numbers[0])  // 1
    console.log(numbers[-1])  // undefined
    console.log(numbers.length) // 5
    
    const numbers = [1,2,3,4,5]
    
    console.log(numbers[numbers.length - 1]) // 5
    console.log(numbers[numbers.length - 2]) // 4
    console.log(numbers[numbers.length - 3]) // 3
    console.log(numbers[numbers.length - 4]) // 2
    console.log(numbers[numbers.length - 5]) // 1
    ```

- 배열 관련 주요 메서드 목록(1) - 기본편(기본 배열 조작)

  - ![image-20220916163511067](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916163511067.png)

  - array.reverse()

    - 원본 배열의 요소들의 순서를 반대로 정렬

    - ```javascript
      const numbers = [1,2,3,4,5]
      numbers.reverse()
      console.log(numbers) // [5,4,3,2,1]
      ```

  - array.push()

    - 배열의 가장 뒤에 요소 추가

  - array.pop()

    - 배열의 마지막 요소 제거

  - ```javascript
    const numbers = [1,2,3,4,5]
    
    numbers.push(100)
    console.log(numbers) // [1,2,3,4,5,100]
    
    numbers.pop()
    console.log(numbers) // [1,2,3,4,5]
    ```

  - array.unshift()

    - 배열의 가장 앞에 요소 추가

  - array.shift()

    - 배열의 첫번째 요소 제거

  - ```javascript
    const numbers = [1,2,3,4,5]
    
    numbers.unshift(100)
    console.log(numbers) // [100,1,2,3,4,5]
    
    numbers.shift()
    console.log(numbers) // [1,2,3,4,5]
    ```

  - array.includes(value)

    - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

    - ```javascript
      const numbers = [1,2,3,4,5]
      
      console.log(numbers.includes(1)) // true
      
      console.log(numbers.includes(100)) // false
      ```

  - array.indexof(value)

    - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환

    - 만약 해당 값이 없을 경우 -1 반환

    - ```javascript
      const numbers = [1,2,3,4,5]
      let result
      
      result = numbers.indexOf(3) //2
      console.log(result)
      ```

  - array.join([separator])

    - 배열의 모든 요소를 연결하여 반환

    - separator(구분자)는 선택적으로 지정가능하며, 생략 시 쉼표를 기본 값으로 사용

    - ```javascript
      const numbers = [1,2,3,4,5]
      let result
      
      result = numbers.join()  // 1,2,3,4,5
      console.log(result)
      
      result = numbers.join('') // 12345
      console.log(result)
      
      result = numbers.join(' ') // 1 2 3 4 5
      console.log(result)
      
      result - numbers.join('-') // 1-2-3-4-5
      console.log(result)
      ```

  - Spread operator를 사용하면 배열 내부에서 배열전개 가능

    - ES5까지는 Array.concat() 메서드를 사용.

  - 얕은 복사에 활용 가능

  - ```javascript
    const array = [1,2,3]
    const newArray = [0, ...array,4]
    
    console.log(newArray)  //[0,1,2,3,4]
    ```

- 배열 관련 주요 메서드 목록 - 심화편

- 메서드 호출 시 인자로 callback 함수를 받는 것이 특징

  - ![image-20220916165032378](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916165032378.png)

  - array.forEach(callback(element[,index[,array]]))

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수는 3가지 매개변수로 구성
      - element: 배열의 요소
      - index: 배열 요소의 인덱스
      - array : 배열 자체
    - return 이 없는 메서드

  - ```javascript
    array.forEach((element,index,array) => {})
    const fruits = ['딸기', '수박' , '사과', '체리']
    
    fruits.forEach((fruits,index) => {
        console.log(fruits,index)
        // 딸기 0
        // 수박 1
        // 사과 2
        // 체리 3
    })
    ```

  - array.map(callback(element[,index[,array]]))

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
    - 기존 배열 전체를 다른 형태로 바꿀 때 유용

  - ```javascript
    array.map((element,index,array)=>{})
    const numbers = [1,2,3,4,5]
    
    const doubleNums = numbers.map((num) => {
        return num * 2
    })
    console.log(doubleNums) // [2,4,6,8,10]
    ```

  - array.filter(callback(element[,index[,array]]))

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
    - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
    - 기존 배열의 요소들을 필터링할 때 유용

  - ```javascript
    array.filter((element,index,array) => {})
    const numbers = [1,2,3,4,5]
    
    const oddNums = numbers.fillter((num,index) => {
        return num % 2
    } 
    console.log(oddNums) // 1,3,5                                
    ```

  - array.reduce(callback(acc,element,[index[,array]])[,initialValue])

    - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

    - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

    - reduce 메서드의 주요 매개변수

      - acc
        - 이전 callback 함수의 반환 값이 누적되는 변수
      - initialValue(optional)
        - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

    - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

    - ```javascript
      array.reduce((acc,element,index,array) => { })
      
      const numbers = [1,2,3]
      
      const result = numbers.reduce((acc,num) => {
          return acc + num
      }, 0)
      
      console.log(result) // 6
      ```

    - ![image-20220916170939043](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220916170939043.png)

  - array.find(callback(element[,index[,array]]))

    - 배열의 각 요소에 대해 콜백 함수를 한번씩 실행

    - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환

    - 찾는 값이 배열에 없으면 undefined 반환

    - ```javascript
      array.find((element,index,array)){}
      
      const avengers = [
          {name: 'Tony Stark', age: 45},
          {name: 'Steve Rogers', age: 32},
          {name: 'Thor', age: 40},
      ]
      const result = avengers.find((avenger) =>{
          return avenger.name === 'Tony Stark'
      })
      
      console.log(result) // {name: 'Tony Stark', age : 45}
      ```

  - array.some(callback(element[,index[,array]]))

    - 배열의 요수 중 하나라도 주어진 판별 함수를 통과하면 참을 반환

    - 모든 요소가 통과하지 못하면 거짓 반환

    - 빈 배열은 항상 거짓 반환

    - ```javascript
      array.some((element,index,array)=> {})
      
      const numbers = [1,3,5,7,9]
      
      const hasEvenNumber = numbers.some((num)=> {
          return num % 2 ===0
      })
      console.log(hasEvenNumber) // false
      
      const hasOddNumber = numbers.some((num)=>{
          return num % 2
      })
      console.log(hasOddNumber) // true
      ```

  - array.every(callback(element[,index[,array]]))

    - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환

    - 하나의 요소라도 통과하지 못하면 거짓 반환

    - 빈 배열은 항상 참 반환

    - ```javascript
      array.every((element,index,array) => {})
      
      const numbers = [2,4,6,8,10]
      
      const isEveryNumberEven = numbers.every((num) => {
          return num % 2 === 0
      })
      console.log(isEveryNumberEven) // true
      
      const isEveryNumberOdd = numbers.every((num)=> {
          return num % 2
      })
      console.log(isEveryNumberOdd) // false
      ```

- 객체

  - 객체는 속성의 집합이며, 중괄호 내부에 key 와 value 의 쌍으로 표현

  - key 는 문자열 타입만 가능

    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어 표현

  - value는 모든 타입 가능

  - 객체 요소 접근은 점 또는 대괄호로 가능

    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

    - ```javascript
      const me = {
          name: 'jack',
          number: '01012345678',
          'samsung': {
          	buds: 'Galaxy Buds',
          	phone: 'Galaxy s21',
      	},
      }
      
      console.log(me.name) //jacl
      console.log(me.number) // 01012345678
      console.log(me['samsung']) // {buds: 'Galaxy Buds', phone: 'Galaxy s21'}
      console.log(me['samsung'].buds) // Galaxy Buds
      ```

  - 메서드는 객체의 속성이 참조하는 함수

  - 객체,메서드명() 으로 호출 가능

  - 메서드 내부에서는 this 키워드가 객체를 의미함

  - ```javascript
    const me = {
        firstName: 'John',
        lastName: 'Doe',
        getFullName: function () {
            return this.firstName + this.lastName
        }
    }
    ```

- 객체 관련 ES6 문법 익히기

  - ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
    - 속성명 축약
    - 메서드명 축약
    - 계산된 속성명 사용하기
    - 구조 분해 할당
      - 구조 분해 할당을 배열도 가능
    - 객체 전개 구문

- Json(JavaScript Object Notation)

  - key-value 쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
  - 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
    - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석이 필수
  - 자바스크립트에서는 Json을 조작하기 위한 두가지 내장 메서드를 제공
    - Json.parse()
      - Json => 자바스크립트 객체
    - Json.stringify()
      - 자바스크립트 객체 => Json