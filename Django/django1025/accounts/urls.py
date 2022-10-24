from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('<int:pk>/', views.detail, name='detail'),
]
