from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question

def index(request):
    page = request.GET.get('page','1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj
        }
    return render(request, 'articles/question_list.html',context)

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question':question
    }
    return render(request,'articles/question_detail.html',context)