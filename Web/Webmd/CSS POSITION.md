#### CSS POSITION

- 문서 상에서 요소의 위치를 지정

- STATIC: 모든 태그의 기본값(기준 위치)
  
  - 일반적인 요소의 배치 순서에 따름(좌측상단)
  
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 아래는 좌표 프로퍼티(위,아,오,왼)를 사용하여 이동 가능
  
  - reltive(상대위치)
    
    - 자기 자신의 static 위치를 기준으로 이동
    
    - 레이아웃에서 요소가 차지하는 공간은 static 일때와 같음.(normal position 대비 offset)
  
  - absolute(절대위치)
    
    - 요소를 일반적인 문서 흐름에서 제거후 레이아웃에 공간을 차지하지않음(normal flow에서 벗어남)
    - static 이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)
  
  - fixed(고정위치)
    
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow 에서 벗어남)
  
  - sticky(스크롤에 따라 static->fixed)(다음주내용)
    
    - 속성을 적용한 박스는 평소에 문서안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed 와 같이 박스를 화면에 고정할 수 있는 속성

- ex:



<img title="" src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-10-40-image.png" alt="" width="369">

<img title="" src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-10-57-image.png" alt="" width="368">

<img title="" src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-11-10-image.png" alt="" width="366">

<img title="" src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-11-27-image.png" alt="" width="367">

<img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-12-23-image.png" title="" alt="" width="374">

<img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-12-34-image.png" title="" alt="" width="374">

- position sticky
  
  - sticky: 스크롤에 따라 static -> fixed 로 변경
    
    - 속석을 적용한 박스는 평소에 문서 안에서 position: static 상태과 같이 일반적인 흐름에 따르지만, 스크롤 위치가 임계저에 이르면 position: fixed 와 같이 박스를 화면에 고정할 수 있는 속성
    
    - 일반적으로 네비게이션 바에서 사용된다.



##### css원칙

- css 원칙 1,2 : Normal flow
  
  - 모든 요소는 네모, 좌측 상단에 배치
  
  - display 에 따라 크기와 배치가 달라짐.

- css 원칙 3
  
  - position 으로 위치의 기준을 변경
    
    - relative: 본인의 원래위치
    
    - absolute: 특정 부모의 위치
    
    - fixed: 화면의 위치
    
    - sticky: 기본적으로 static 이나 스크롤이동에 따라 fixed 로 변경

##### CSS Layout

- Display

- Position

- Float (CSS1,1996)

- Flexbox (2012)

- Grid (2017)

- 기타
  
  - Reponsive Web Design(2010),Media Queries(2012)

##### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함

- 요소가 normal flow를 벗어나도록 함

<img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-15-32-image.png" title="" alt="" width="444">

<img title="" src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-11-22-58-image.png" alt="" width="444">

##### Flexbox

- (CSS Flexibl Box Layout)행과 열 형태로 하이템들을 배치하는 1차원 레이아웃 모델

- 축
  
  - main axis
  
  - cross axis

- 구성요소
  
  - Flex container (부모요소)   
    
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    
    - Flex item 들이 놓여있는 영역
    
    - display 속성을 flex 혹은 inline-flex로 지정
  
  - Flex item (자식요소)
    
    - 컨테이너에 속해있는 컨텐츠

- 예시



![](C:\Users\wnsgh\AppData\Roaming\marktext\images\2022-08-31-11-26-47-image.png)

- flex 사용이유
  
  - 수직정렬
  
  - 아이템의 너비 혹은 간격을 동일하게 배치

- Flex 속성
  
  - 배치설정
    
    - flex-direction
    
    - flex-wrap
  
  - 공간나누기
    
    - justify-content(main axis)
    
    - align-content(cross axis)
  
  - 정렬
    
    - align-items
    
    - align-self
  
  - Main axis 기준 방향 설정
  
  - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-18-53-image.png" title="" alt="" width="444">

- flex-wrap
  
  - 아이템이 컨테이너를 벗어나는 경우 해당 영역내에 배치되도록 설정
  
  - 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-11-35-16-image.png" title="" alt="" width="431">

- flex-direction:

- flex-wrap:
  
  - nowrap:한줄에 배치
  
  - wrap: 넘치면 그다음줄로 배치

- flex-flow
  
  - flex-direction과 flex-wrap 의 shorthand
  
  - flex-direction과 flex-wrap 에 대한 설정값을 차례로 작성
  
  - ex) flex-flow: row nowrap;

- justify-content
  
  - main axis 를 기준으로 공간배분
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-11-36-33-image.png" title="" alt="" width="455">
  
  - 공간 배분
    
    - flex-start (기본 값) : 아이템들을 axis 시작점으로
    
    - flex-end : 아이템들을 axis 끝 쪽으로
    
    - center : 아이템들을 axis 중앙으로
    
    - space-between : 아이템 사이의 간격을 균일하게 분배
    
    - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
    
    - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배

- align-items
  
  - 모든 아이템을 Cross axis 를 기준으로 정렬
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-11-38-14-image.png" title="" alt="" width="435">

- align-self
  
  - 개별아이템을 Cross axis 기준으로 정렬
    
    - 주의! 해당속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용
    - stretch (기본 값) : 컨테이너를 가득 채움
    - flex-start : 위
    - flex-end : 아래
    - center : 가운데
    - baseline : 텍스트 baseline에 기준선을 맞춤

- 기타속성
  
  - flex-grow : 남은 영역을 아이템에 분배(비율)
  
  - order : 배치순서
  
  - <img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-23-49-image.png" title="" alt="" width="437">

<img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-24-33-image.png" title="" alt="" width="459"><img src="file:///C:/Users/wnsgh/AppData/Roaming/marktext/images/2022-08-31-15-24-27-image.png" title="" alt="" width="456">
