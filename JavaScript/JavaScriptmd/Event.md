#### Event

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음.
  - 특정 메서드를 호출하여 프로그래밍적으로도 만들어낼수 있음.
  - ![image-20220919140156657](C:\Users\wnsgh\AppData\Roaming\Typora\typora-user-images\image-20220919140156657.png)

- Event handler - addEventListener()
  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능
- Event handler - addEventListener(type,listener[,options])
  - type
    - 반응 할 이벤트 유형
  - listener
    - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체 EventListener 인터페이스 혹은 JS function 객체여야함.
- Event 취소
  - event.preventDefault()
  - 현재 이벤트의 기본 동작을 중단
  - HTML 요소의 기본 동작을 작동하지 않게 막음
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지않고 그 이벤트를 취소
  - 취소할수 없는 이벤트
    - event.cancelable을 통해 확인 가능

