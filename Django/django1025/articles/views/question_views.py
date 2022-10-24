from email import message
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import QuestionForm
from django.contrib import messages
from ..models import Question

@login_required(login_url='accounts:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('articles:index')
    else:
        form = QuestionForm()
    context = {
        'form':form
    }
    return render(request, 'articles/question_form.html',context)


@login_required(login_url='accounts:login')
def question_modify(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.author:
        messages.error(request,'수정권한이 없습니다.')
        return redirect('articles:detail',pk=pk)
    
    if request.method == "POST":
        form = QuestionForm(request.POST,instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('articles:detail', pk=pk)
    
    else:
        form = QuestionForm(instance=question)
    context = {
        'form':form
    }
    return render(request, 'articles/question_form.html',context)


@login_required(login_url='articles:login')
def question_delete(request,pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.author:
        messages.error(request,'삭제 권한이 없습니다.')
        return redirect('articles:detail', pk=pk)
    question.delete()
    return redirect('articles:index')


@login_required(login_url='articles:login')
def question_vote(request,pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user in question.voter.all():
        question.voter.remove(request.user)
    else:
        question.voter.add(request.user)
    return redirect('articles:detail', pk=question.id)