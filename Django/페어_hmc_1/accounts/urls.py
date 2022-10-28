from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:pk>/update/',views.update,name="update"),
    path('login/',views.login,name="login"),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ID_delete/', views.ID_delete, name='ID_delete'),
    path('<int:pk>/', views.detail, name='detail'),
]