# 빠른 시작을 위한 Django 프로젝트 기본 가이드

## 프로젝트 생성

#### 가상환경 생성

```
# 가상환경 생성
python -m venv venv
```

#### 가상환경 실행

```
# 가상환경 실행
. venv/scripts/activate
```

#### 패키지 설치

```
# 미리 준비된 패키지 일괄 설치
pip instrall -r requirements.txt
```

#### 프로젝트 생성 및 앱 생성

```
django-admin startproject pjt . #pjt는 프로젝트명
python manage.py startapp {app name} # 프로젝트 내부 각 앱마다 생성
```

#### 모델 마이그레이션

> **주의: 마이그레이션은 마지막에 실행 할 것!**
>
> - 프로젝트 도중 모델을 수정하게 될 경우 에러가 발생한다.

```
python manage.py makemigrations

python manage.py migrate
```

#### 데이터베이스 초기화

> - migrations 파일 삭제
> - migrations 폴더 및 **init**.py는 삭제하지 않음
> - 번호가 붙은 파일만 삭제
> - db.sqlite3 삭제

#### 서버 실행

```
python manage.py runserver
```

### 프로젝트 기본 템플릿 폴더

```
#pjt/templates
base.html # 각 페이지의 기본 바탕이 되는 기초 페이지
root.html # 루트 페이지 http://127.0.0.1:8000/
```

## 프로젝트 기본 설정

### 프로젝트 보안 설정

```
#pjt/setting.py
# 보안을 위한 SECRET_KEY 분리
import os, json
from django.core.exceptions import ImproperlyConfigured

...


secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# 상위 폴더의 secrets.json에 생성된 SECRET_KEY를 딕셔너리 형태로 저장
# secrets.json은 gitignore로 설정해서 업로드 안되게 하자
```

### 앱 설정

```
#pjt/setting.py
INSTALLED_APPS = [
    "articles", # 생성한 앱1
    "accounts", # 생성한 앱2
    "django_bootstrap5", # 부트스트랩을 적용시켜주자
    ...
```

### 부트스트랩 확장을 위한 설정

```
#pjt/setting.py
TEMPLATES = [
            ...
             "DIRS": [BASE_DIR / "pjt" / "templates"],
            ...
```

### 시간대 설정

```
#pjt/setting.py
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

### 커스텀 유저 Auth 설정

```
#pjt/setting.py
AUTH_USER_MODEL = "accounts.User"
```

### 프로젝트 URL 설정

```
#pjt/urls.py
from . import views
...
from django.urls import path, include

...
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.root), # 루트 페이지 호출
    # 프로젝트 내부의 각 앱들 마다 설정
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
]
```

## accounts 앱

### user 생성, 그 리스트, user의 상세 정보를 출력

```
accounts
├── templates/accounts
│               ├── index.html  # 생성된 user 리스트 출력
│               ├── signup.html # user 생성
│               └── detail.html # user의 상세 정보 출력
```

### admin 설정

```
#accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model(), UserAdmin)
```

### user 생성을 위한 입력 form 설정

```
#accounts/forms.py
# from .models import User
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )
```

### DB에 저장 하기 위한 데이터 형식 설정

```
#accounts/models.py
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

### accounts 앱을 표시 위한 URL 설정

```
#accounts/urls.py
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("<int:pk>/", views.detail, name="detail"),
]
```

### accounts 앱을 구동을 위한 view 설정

```
#accounts/views.py
from django.shortcuts import render, redirect


# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import User

# from .models import User
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    users = User.objects.all()
    # Template에 전달한다.
    context = {"users": users}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {"user": user}
    return render(request, "accounts/detail.html", context)
```

## articles 앱

### articles 구조

```
articles
├── templates/articles
│               ├── index.html  # 생성된 article 리스트 출력
│               ├── form.html   # article 생성
│               └── detail.html # article의 상세 정보 출력
```

### admin 설정

```
#articles/admin.py
from django.contrib import admin
from .models import Article

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


admin.site.register(Article, ArticleAdmin)
```

### article 생성을 위한 입력 form 설정

```
#articles/forms.py
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
```

### DB에 저장 하기 위한 데이터 형식 설정

```
#articles/models.py
from django.db import models

# Create your models here.
"""
게시판 기능 
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
"""
# 1. 모델 설계 (DB 스키마 설계)
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### articles 앱을 표시 위한 URL 설정

```
#articles/urls.py
# URL설정을 app 단위로!
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]
```

### articles 앱을 구동을 위한 view 설정

```
#articles/views.py
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {"article": article}
    return render(request, "articles/detail.html", context)
```