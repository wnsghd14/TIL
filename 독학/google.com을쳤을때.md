1. 브라우저에 검색창에 'www.google.com'을 입력 후. 엔터를 친다.
   - 특정 웹사이트에 접속하기 위해서는 'www.google.com' 과 같은 도메인(Domain)이 아닌 '127.0.0.1'과 같은 IP 주소가 필요하다.
     하지만 IP 주소는 외우기가 힘들고, 가독성이 떨어지기 때문에 도메인 명으로 웹페이지에 접속할 수 있도록 DNS 서버를 이용한다.
     DNS는 Domain Name System의 약자로 URL의 이름과 IP주소를 저장하고 있는 데이터베이스이다. (like 전화번호부)


2. 브라우저는 캐싱된 DNS 기록을 체크한다.
   - 브라우저는 4가지 캐시를 확인한다. (Browser캐시 >OS 캐시 (systemcall) > router 캐시 > ISP 캐시
     캐시는 네트워크 트랙픽 조절과 데이터 전송 시간을 줄여준다.
     ISP는 인터넷 서비스 공급자의 약자이다. ex) SK, LG, KT 등


3. 요청한 URL이 캐시에 없으면, ISP의 DNS 서버에서 다른 DNS 서버를 DNS Query를 통해 검색하여 IP 주소를 찾는다.
   - 캐시에 요청한 URL의 IP 정보가 없으면, ISP는 DNS 서버들을 검색해 해당 도메인의 IP 주소를 검색한다.
     해당 검색기법을 recursive search라 부르며, IP 주소를 찾을 때까지, DNS 서버에서 다른 DNS 서버를 오가면서 반복 검색을 진행한다.


4. 브라우저가 서버와 TCP connection을 한다.
   - 브라우저가 IP 주소를 얻게되면 서버와 http connection을 통해 서버와 연결을 한다.
     HTTP 연결의 경우 대표적인 인터넷 프로토콜인 TCP를 일반적으로 사용한다.
     TCP/IP three-way handshake라는 프로세스를 통해서 클라이언트와 서버간 connection이 이뤄지게 된다. 


5. Browser가 웹서버에 HTTP 요청을 한다.
   - TCP 연결이 되면, 데이터 전송을 하면된다.
     클라이언트는 GET 요청을 통해 서버에서 'www.google.com' 웹페이지를 요구한다.
     요청에 따라 부가적인 정보들이 함께 전송되는데 개발자 도구의 network에서 자세한 내용을 확인할 수 있다.


6. 서버가 요청을 처리하고, response를 생성한다.
   - 서버가 가지고 있는 웹서버에서 브라우저로부터 온 요청을 읽고 response를 생성한다.
     response를 특정한 포맷(JSON, XML, HTML)으로 작성한다.


7. 서버가 HTTP Response를 보낸다.
   - 서버의 response에는 요청한 웹페이지, 상태코드, 쿠키, 개이정보 등이 포함되어있다.


8. 브라우저가 HTML content를 보여준다.
   - 브라우저는 html content를 단계적으로 렌더링 하여 노출한다.
     해당 contents 들은 브라우저에 의해 캐싱되어 나중에 해당 페이지 재방문시 서버에 재요청하지 않도록 한다.
     그 이후, 'www.google.com' 웹 페이지가 노출된다.
