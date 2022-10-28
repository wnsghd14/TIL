from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image", "otwo", "workout", "part"]
        labels = {
            "title": "질문",
            "content": "질문내용",
            "otwo": "운동 종류",
            "part": "자극부위 선택",
            "workout": "종목",
        }


class MakeCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
