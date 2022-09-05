##### HTML 문서구조화

- table의 각 영역을 명시하기 위해 <thead> <tbody> <tfoot>요소를 활용(필수X)
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-09-05-13-42-39-image.png" title="" alt="" width="320">

- tr 으로 가로 줄을 구성하고 내부에는 tr 혹은 td 로 셀을 구성
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-09-05-13-43-41-image.png" title="" alt="" width="318">

- colspan,rowspan 속성을 활용하여 셀 병합
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-09-05-13-43-50-image.png" title="" alt="" width="323">

- caption 을 통해 표 설명 또는 제목을 나타냄
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-09-05-13-44-21-image.png" title="" alt="" width="284">

- table 태그 기본구성html
  
  ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-44-36-image.png)
  
  - thead
    
    - tr > th
  
  - tbody
    
    - tr > td
  
  - tfoot
    
    - tr > td
  
  - caption

##### form

- form 은 정보를 서버에 제출하기 위해 사용하는 태그
- form 기본속성
  - action: form 을 처리할 서버의 url(데이터를 보낼 곳)
  - method: form을 제출할때 사용할 HTTP 메서드(GET or POST)
  - enctype: 메서드가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded:  기본값
    - multipart/form-data : 파일 전송시(input type 이 file 인 경우)
    - ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-46-43-image.png)

##### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  
  - input의 대표적인 속성
    
    - name : form 컨트롤에 적용되는 이름
    
    - value : form 컨트롤에 적용되는 값.
    
    - required, readonly, autofocus, autocomplete, disabled 등
    
    - ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-48-25-image.png)![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-48-17-image.png)
    
    - ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-48-51-image.png)

- input label
  
  - label 을 클릭하여 input자체의 초점을 맞추거나 활성화 시킬수 있음
    
    - 사용자는 선택할 수 있는 영역이 늘어나 웹/ 모바일환경에서 편하게 사용할 수 있음
    
    - label 과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label 을 읽어 쉽게 내용을 확인 할수있도록 함
  
  - input에 id 속성을, label 에는 for 속성을 활용하여 상호 연관을 시킴.
    
    - ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-49-37-image.png)

##### input 유형-일반

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  
  - text : 일반 텍스트 입력
  
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  
  - file : accept 속성을 활용하여 파일 타입 지정 가능

##### input 유형- 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택항목을 작성함

- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야함
  
  - checkbox: 다중 선택
  
  - radio:단일 선택

##### input 유형-기타

- 다양한 종류의 input을 위한 picker를 제공
  
  - color : color picker
  
  - date : date picker

- hidden input 을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  
  - hidden : 사용자에 보이지 않는 input

##### Bootstrap

- CDN
  
  - 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

- spacing
  
  ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-13-58-24-image.png)
  
  - property
    
    - m - margin
    
    - p - padding
  
  - sides
    
    - t - margin-top or padding-top
    
    - b - margin-bottom or padding-bottom
    
    - s - margin-left or padding-left in LTR, margin-right or padding-right in RTL
    
    - e - margin-right or padding-right in LTR, margin-left or padding-left in RTL
    
    - x - left and right
    
    - y - top and bottom
    
    - blank -  margin or padding on all 4 sides of the element
  
  - size
    
    - 0 - that eliminate the margin or padding by setting it to 0
    
    - 1 - that set the margin or padding to $sapcer 0.25rem 4px
    
    - 2 - that set the margin or padding to $spacer 0.5rem 8px
    
    - 3 - that set the margin or padding to $spacer 1rem 16px
    
    - 4 - that set the margin or padding to $spacer 1.5rem 24px
    
    - 5 - that set the margin or padding to $spacer 3rem 48
  
  - mx-0 : 블록요소 수평중앙정렬 가로가운데정렬 (important)
  
  - py-0 : 위아래 패딩이 0(!important)

- color
  
  - ![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-09-05-14-17-09-image.png)

##### Display

- 공식문서를 보며 진행.
