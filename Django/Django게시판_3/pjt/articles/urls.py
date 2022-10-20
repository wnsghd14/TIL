from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'articles'

urlpatterns = [
    # base views.py
    path('', base_views.index, name='index'),
    path('<int:pk>/',base_views.detail, name='detail'),
    
    # question_views.py
    
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:pk>/', question_views.question_modify, name="question_modify"),
    path('question/delete/<int:pk>/' , question_views.question_delete, name="question_delete"),
    # recommend
    path('question/vote/<int:pk>/', question_views.question_vote, name="question_vote"),

    # answer_views.py
    path('answer/create/<int:pk>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:pk>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:pk>/', answer_views.answer_delete, name='answer_delete'),
    # recommend
    path('answer/vote/<int:pk>/', answer_views.answer_vote, name='answer_vote'),

    
]