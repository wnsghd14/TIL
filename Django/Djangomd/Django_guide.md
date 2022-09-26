1. python -m venv (venv_name) : 가상환경 만들기
2. source(or .) (venv_name)/Scripts/activate : 가상환경 실행
3. pip install django==3.2.13 : 쟝고 다운로드
4. django-admin startproject (project_name) . : .중요 현재 폴더에 프로젝트 생성
5. python manage.py runserver : 서버 작동 (현재폴더에서 만들지 않았을 경우 cd를 활용해 manage.py를 찾은 후 실행한다.)(ctrl + c 로 종료 가능)
6. python manage.py startapp (app_name) : 앱 만들기.
7. project 폴더에서 settings.py 안의 install_apps 리스트의 안에 'app_name', 넣어주기 (콤마가 중요!)
8. app_name 폴더안에 'templates'라는 폴더 생성!
9. project_name 폴더안의 urls.py 파일안에서 
   1.  from app_name import views 선언
   2.  urlpatterns 리스트에 path('도메인뒷부분이름',views.함수이름)
10. app_name 폴더안 views.py 에 def 함수이름(request): return render(request,'도메인이름' ) 선언.