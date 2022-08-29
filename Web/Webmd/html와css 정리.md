#### HTML

- Hyper Text Markup Language
- 마크업 언어로 웹 문서를 작성하며, tag를 사용하여 문서의 구조 등을 기술하는 언어.

#### Web & HTML 작동원리

- 서버는 클라이언트의 요청을 분석하여 결과값을 HTML로 전송하고 연결 종료.
- 클라이언트는 서버로부터 전달받은 HTML을 Web Browser에 표시
- 각 Web Browser는 브라우저 엔진이 내장되어 있고, 이 엔진이 tag를 해석하여 화면에 표현

### Body 요소

- id 속성을 이용하여 문서 내에서 tag를 유일하게 식별 가능 (id속성은 중복 X)
- class 속성을 이용하여 여러 tag에 공통적인 특성(CSS)을 부여 (class 속성은 중복 O)



#### section

- section 태그를 이용하면 같은 태그를 서로 다르게 표현할 수 있다.

#### 특수문자

| 엔터티이름     | 설명            | 출력  |
| --------- | ------------- | --- |
| & + nbsp; | 공백            |     |
| &  + gt   | Greater than  | <   |
| & + lt    | Ampersand     | >   |
| & + quot  | qutation mark | &   |
| & + amp   | Ampersand     | &   |



#### 목록형 요소

- ul : 번호없는 목록을 표시
- ol : 번호있는 목록을 표시
- li : 목록 항목 - ul, ol 하위에서 사용
- dl : 용어 정의와 설명에 대한 내용을 목록화해서 표시
- dt : 용어 목록의 정의 부분을 나타냄
- dd : 용어 목록의 설명 부분을 나타냄

### 링크 요소

#### target

| 속성      | 설명                              |
| ------- | ------------------------------- |
| _blank  | 링크 내용이 새창이나 새탭에서 열림.            |
| _self   | target 속성의 기본 값                 |
| _parent | 프레임을 사용했을 때 링크내용을 부모 프레임에 표시    |
| _top    | 프레임을 사용했을 때 프레임에서 벗어나 전체화면으로 표시 |



#### anchor

```xml
<a href="#menu"></a>
```

- id 값이 menu인 위치로 이동

### Form control

- 데이터를 입력 받아 서버에 처리하기 위한 용도로 사용

```stata
<form method="post" action ="login.jsp">  <li>      <label for="userid">아이디 : </label>    <input type="text" id = "userid" name="userid">  </li>  <li>      <label for="pass">아이디 : </label>    <input type="text" id = "pass" name="pass">  </li>  <li><input type="submit" value="로그인"></li></form>
```

| tag      | 설명                                           |
| -------- | -------------------------------------------- |
| form     | 사용자에게 입력 받을 항목을 정의.                          |
| input    | 텍스트 box,체크box,라디오 버튼 등 사용자가 데이터를 입력할수 있도록 함. |
| textarea | 여러줄의 문자를 입력할수 있도록 함                          |
| button   | 버튼을 표시                                       |
| select   | select box(dropdown,combobox) 를 표시           |
| optgriup | select box의 각 항목들을 그룹화함                      |
| option   | select box 의 각 항목들을 그룹화 함                    |
| label    | 마우스를 이용하여 <input> 항목을 선택시 편리함을 제공.           |
| fieldset | 입력항목들을 그룹화 함                                 |
| legend   | <fieldset>의 제목을 지정함                          |



- Form control 요소들

#### method

- 사용자가 입력한 내용을 서버 쪽으로 어떻게 넘겨줄지 지정
- GET : url에 입력한 내용이 쿼리스트링 형식으로 표시 (256 ~ 2048바이트로 길이 제한)
- POST : HTTP 메시지의 Body에 담아서 전송하기 때문에 전송 내용의 길이에 제한이 없다. url에 입력한 내용이 표시되지 않는다.

#### action

- form 태그 안의 내용들을 처리해 줄 서버 상의 url 지정
- 현재 페이지 즉, 자기 자신이라면 생략 가능하다.

#### submit

- form 태그에서 전송을 하는 기능
- 만약 보내지는 기능을 유효성 검사 등으로 예외처리를 하고 싶은 경우 preventDefault 또는 이벤트 핸들러가 return false 를 출력하도록 만들어 강제로 넘어가는 것을 백엔드에서 방지할 수 있다.

### div & span

| 태그   | 설명                                                                                    |
| ---- | ------------------------------------------------------------------------------------- |
| div  | block 형식으로 공간을 분할, 웹사이트의 레이아웃을 만들때 사용 div 태그를 사용하여 각각의 블록을 알맞게 배치하고 CSS를 활용하여 스타일을 적용 |
| span | inline 형식으로 공간을 분할 <div> 와 <p> 태그와 함께 웹페이지의 일부분에 스타일을 적용시키기 위해 사용                     |



- 차이점
  - div와 span을 여러 개 만들어 나열했을 때, div는 자동 줄 바꿈이 일어나면서 세로로, span은 줄 바꿈이 일어나지 않고 가로로 나열.
  - 동일한 문장을 감쌌을 때, div는 박스 형태로 영역이 설정되고 그 안에 정렬, span은 줄 단위로 영역이 설정되기 때문에 박스 형태가 아닌 텍스트가 노출되는 영역만 포함.
  - div와 margin은 4방향 모두 적용이 되며, span의 margin은 양옆으로만 적용.

### block & inline

| block 형식 태그 | inlin 형식 태그 |
| ----------- | ----------- |
| h1~h6태그     | a 태그        |
| p 태그        | input 태그    |
| 목록 태그       | 글자형식 태그     |
| table 태그    |             |
| form 태그     |             |



- block : div, inline : span 외에도 여러 태그들이 존재한다.

### Semantic



![image](https://user-images.githubusercontent.com/81945553/159164046-26433549-907f-4939-b0f6-783e6ed36482.png)

- header : 헤더 지정
- nav : 네비게이션 지정
- aside : 본문 이외의 내용 표시
- section : 본문의 여러 내용(article)을 포함
- article : 본문의 주 내용이 포함
- footer : 저작권 표시 등 포함

## CSS

- Cascading Style Sheets : HTML 문서를 화면에 표시하는 방식을 정의한 언어
- 기존 웹 문서를 다양하계 설계하고, 변경 요구 대응에 따르는 어려움을 보완
- 선택자(selector) 와 선언 (declaration : { }) 두 부분으로 구성
- 선언부 안에 속성(property)과 값(value)로 넣으며 ;로 구분

### 스타일 적용 방법

```xml
<!-- 외부 스타일 시트--><link rel="stylesheet" type = "text/css" href="./main.css"> <style type="text/css">@import url("./main.css");</style>
```

- 외부 스타일 시트 적용 방법으로는 link 태그나 @import로 HTMl 문서에 연결하여 사용할 수 있다.

```xml
<style type="text/css">h1 {color: pink;}.classname {background-color: cyan; color: magenta;}</style>
```

- 내부 스타일 시트 방식은 head 안에서 작성한다.

```xml
<p style="background-color:cyan; color:magenta"></p>
```

- 인라인 속성으로 개별 엘리먼트에 스타일을 적용하는 방식 (우선 순위가 가장 높다.)
- 스타일 우선 순위 : 인라인 > 내부 > 외부 순

### Selector

| 선택자         | 의미                    |
| ----------- | --------------------- |
| * {}        | 모든 element            |
| h1,h2,h3 {} | 매칭되는 element          |
| .class{}    | class 명과 매칭되는 element |
| #id{}       | id 값과 매칭되는 element    |
| E1E2{}      | 하위 element 선택         |
| E1>E2{}     | 직속 하위 element 선택      |
| E1+E2{}     | 인접형제 관계인 element 선택   |
| E1~E2{}     | 형제 관계인 element 선택     |



- E1 > E2 : 한단계 아래에 있는 E2에게만 적용
- E1 E2 : E1 아래에 있는 모든 E2에게 적용
- E1 + E2 : 형제 관계가 여러 개일 경우 첫 번째 엘리먼트만 선택
- E1 ~ E2 : 형제 관계가 여러 개일 경우 모든 엘리먼트 선택

#### 가상 클래스 Selector

- first-child : 지정된 요소 중 부모의 첫 번째 자식 선택
- last-child : 지정된 요소 중 부모의 마지막 자식 선택

```css
li:nth-child(5){}li:nth-child(3n+1){} 
```

- nth-child(5) : 지정된 요소 중 n번째 자식 선택

#### 속성 선택자 요소

| 선택자    | 의미                                   |
| ------ | ------------------------------------ |
| [A]    | A 속성이 포함된 ELEMENT 선택                 |
| [A=V]  | A 속성 값이 V와 정확히 일치하는 ELEMENT 선택       |
| [A~=V] | A 속성 값이 V단어를 포함하는 ELEMENT 선택         |
| [A^=V] | A 속성값이 V로 시작하는 ELEMENT 선택            |
| [A*=V] | A 속성값이 V를 포함하는 ELEMENT 선택            |
| [A$=V] | A 속성값이 V로 끝나는 ELEMENT 선택             |
| [AI=V] | A 속성 값이 정확히 V이거나 V-로 시작하는 ELEMENT 선택 |



- 특정한 속성을 가지거나 속상 값을 갖는 엘리먼트를 선택
- Existence : [] , Equality : = , Space : ~=, Prefix : ^=, Substring : *= 등
- ~= : 속성 값이 스페이스로 구분하여 V를 포함하는 지를 판단
- *= : V를 포함하는지를 판단

#### 우선 순위

```css
p li {color : green !important;}p li {color : gray};
```

- 속성 값 뒤에 !import를 작성하면 같은 엘리먼트에 대해 우선적으로 스타일이 적용된다.

### [display 속성]

- display : inline (인라인 형태로 변경 - div 같은 블록 형태를 변경할 때 사용)
- display : block (블록 형태로 변경 - span과 같은 인라인 형태를 변경할 때 사용)
- display : none (안보이게 변경 )

### position

- 엘리먼트의 위치를 고정시키거나 브라우저의 크기에 따라 이동하는 등 동적으로 만들기 위한 기본적인 속성
- static : 기본 값으로 top과 left에서의 거리를 지정할 수 없다.
- relative : top, left 거리를 지정할 수 있다.
- absolute : 자신의 상위 box 속에서의 top, left, right, botton 등의 절대적인 위치를 지정할 수 있다. (단 상위 box는 static이 아니어야 하고 아무 것도 없다면 DOM트리의 최상위에 있는 body가 배치 기준이 된다.)
- fixed : 브라우저 전체 화면을 기준으로 스크롤이 일어나도 항상 화면상의 지정된 위치에 있다.
