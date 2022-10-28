from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/comment/', views.comment, name='comment'),
    path('<int:pk>/like/', views.like, name='like'),
    path('articles/search',views.search,name='search'),
]