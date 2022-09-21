### Django

- Framework
  - Frame(틀) + Work(일하다)
    - 일정한 뼈대 틀을 가지고 일하는것
    - 제공받은 도구들과 틀, 규약을 가지고 무언가를 만드는 것
    - 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
  - 따라서, Framework를 잘 사용하기만 하면 웹 서비스 개발에 있어서 모든 것들을 하나부터 열까지 직접 개발할 필요 없이, 내가 만들고자 하는 본질(로직)에 집중해 개발할 수 있음 
  - 소프트웨어의 생산성과 품질을 높임
- Web
  - 클라이언트 - 서버 구조로 이루어져 있다.
  - Django 는 서버를 구현하는 웹 프레임 워크
- Web browser
  - 웹에서 페이지를 찾아 보여주고, 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
  - 웹페이지 파일을 우리가 보는 화면으로 바꿔주는(렌더링) 프로그램

- Web page
  - 정적 웹페이지
    - Static Web page
    - 있는 그대로를 제공하는 것을 의미
    - 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
    - 같은 상황에서 모든 사용자에게 동일한 정보를 표시
  - 동적 웹페이지
    - Dynamic Web page
    - 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    - 웹 페이지의 내용을 바꿔주는 주체 == 서버
    - 다양한 서버 사이드 프로그래밍 언어(python, java, c++ 등) 사용 가능 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐
- Design Pattern
  - 앞서 배웠던 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
  - 자주 사용되는 소프트웨어의 구조를 소수의 뛰어난 엔지니어가 마치 건축의 공법처럼 일반적인 구조화를 해둔 것
  - 목적 : 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
  - 장점
    - 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐
    - Before
      - "무언가 서비스를 요청을 하는 쪽을 하나 만들고.. 둘 사이에 데이터를 주고 받는 방식을 정의 한 다음.. 요청을 처리하는 쪽을 하나 따로 개발해서.. 다수의 요청을 처리하는 구조로 만들어보자..!"
    - After
      -  "우리 이거 클라이언트-서버 구조로 구현하자"
    - 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙,  커뮤니케이션의 효율성을 높이는 기법
- Django Design Pattern
  - Django에도 이러한 디자인 패턴이 적용이 되어 있는데,  Django에 적용된 디자인 패턴은 MTV 패턴이다
  - MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.
- MVC Design Pattern
  - MVC는 Model - View – Controller의 준말 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
  - 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
  - Model : 데이터와 관련된 로직을 관리, View : 레이아웃과 화면을 처리, Controller : 명령을 model과 view 부분으로 연결
  - 목적
    - 관심사 분리
    - 더 나은 업무의 분리와 향상된 관리를 제공
    - 각 부분을 독립적으로 개발할 수 있어, 하나를 수정하고 싶을 때 모두 건들지 않아도 됨
      - 개발 효율성 및 유지보수가 쉬워짐
      - 다수의 멤버로 개발하기 용이함
- MTV (Model Template View)
  - Model 
    - MVC 패턴에서 Model의 역할에 해당 
    - 데이터와 관련된 로직을 관리 
    - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
  - Template
    - 레이아웃과 화면을 처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    - MVC 패턴에서 View의 역할에 해당
  -  View
    - Model & Template과 관련한 로직을 처리해서 응답을 반환
    - 클라이언트의 요청에 대해 처리를 분기하는 역할
    - 동작 예시
      -  데이터가 필요하다면 model에 접근해서 데이터를 가져오고 가져온 데이터를 template로 보내 화면을 구성하고 구성된 화면을 응답으로 만들어 클라이언트에게 반환
    - MVC 패턴에서 Controller의 역할에 해당
    - ![화면 캡처 2022-09-21 144121](Django2.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-09-21%20144121.png)

- Django 설치

  - Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치

  - ```bash
    $ pip install django==3.2.13
    $ pip freeze > requirements.txt
    ```

- LTS

  - Long Term Support 
  - 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
  - 컴퓨터 소프트웨어의 제품수명주기 관리 정책
  - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함
  - __init__.py 
    - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
    - 별도로 추가 코드를 작성하지 않음
  - asgi.py 
    - Asynchronous Server Gateway Interface 
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움 
    - 추후 배포 시에 사용하며 지금은 수정하지 않음
  - settings.py 
    - Django 프로젝트 설정을 관리
  - urls.py 
    - 사이트의 url과 적절한 views의 연결을 지정
  - wsgi.py 
    - Web Server Gateway Interface 
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움 
    - 추후 배포 시에 사용하며 지금은 수정하지 않음
  - manage.py 
    - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

- Django Application

  - 애플리케이션(앱) 생성

  - ```bash
    $ python manage.py startapp articles
    ```

  - admin.py 

    - 관리자용 페이지를 설정 하는 곳

  - apps.py 

    - 앱의 정보가 작성된 곳 
    - 별도로 추가 코드를 작성하지 않음

  - models.py 

    - 애플리케이션에서 사용하는 Model을 정의하는 곳 
    - MTV 패턴의 M에 해당

  - tests.py 

    - 프로젝트의 테스트 코드를 작성하는 곳

  - views.py 

    - view 함수들이 정의 되는 곳 
    - MTV 패턴의 V에 해당

  - 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 반드시 추가해야 함

  - INSTALLED_APPS

    -  Django installation에 활성화 된 모든 앱을 지정하는 문자열 목록

    - ```python
      INSALLED_APPS = [
          'articles',
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
      ]
      # 반드시 생성 후 등록
      ```

  - 해당 순서를 지키지 않아도 수업 과정에서는 문제가 없지만, 추후 advanced 한 내용을 대비하기 위해 지키는 것을 권장

    - ```python
      INSTALLED_APPS = [
          # Local apps
          'articles',
          # Third party apps
          'haystack',
          # Django apps
          'django.contrib.admin'
          ,
          'django.contrib.auth'
          ,
          'django.contrib.contenttypes'
          ,
          'django.contrib.sessions'
          ,
          'django.contrib.sites',
      ]
      ```