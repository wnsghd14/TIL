## Django Crud

1. python -m venv 가상환경이름
2. source 가상환경이름/Scripts/activate
3. pip install django==3.2.13
4. pip freeze > requirements.txt
5. django-admin startproject 프로젝트이름 경로(. 이 보편적)
  - 혹시나 경로설정 안했을 경우 ls 를 통해 manage.py가 있는 경로에 들어가야 한다.(cd 프로젝트이름)
6. python manage.py startapp articles(앱이름)
7. config 파일내에 있는 settings.py에 들어가  installed apps 리스트안에 '앱이름', 을 작성한다.
8. config 파일내에 있는 urls.py에서 urlpatterns 에 path('url이름/', include('articles.urls')), 를 입력한다.
9. articles 폴더 내에 urls.py 라는 파일을 만들어 준다.

     - from django.urls import path 입력
     - from . import views 입력
     - app_name = 앱이름 입력
     - urlpatterns 라는 리스트 생성후 그 안에 path('',views.index) 입력
10. articles 폴더 내에 있는 views.py 파일에서

      - def index(request):
      -   return render(request,'index.html') 을 입력.
11. articles 폴더에서 templates 폴더 생성
12. templates 폴더내에서 articles(앱이름) 라는 폴더 생성
13. templates/articles 폴더내에서 index.html 파일 생성
14. models.py 클래스 생성 후 python manage.py makemigrations 마이그레이션 파일 생성
15. python manage.py migrate 후 db.sqlite3에서 데이터베이스 확인!
