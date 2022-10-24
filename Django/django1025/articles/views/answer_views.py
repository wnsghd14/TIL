from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from ..models import Question, Answer
from ..forms import AnswerForm
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages


@login_required(login_url='accounts:login')
def answer_create(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('articles:detail', pk=pk), answer.id))
    else:
        form = AnswerForm()
    context = {
        'question':question,
        'form' : form
    }
    return render(request,'articles/question_detail.html',context)


@login_required(login_url='articles:login')
def answer_modify(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('articles:detail', pk=answer.question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('articles:detail', pk=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {
        'answer': answer,
        'form': form
    }
    return render(request, 'articles/answer_form.html',context)


@login_required(login_url='articles:login')
def answer_delete(request,pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user != answer.author:
        messages.error(request,'삭제 권한이 없습니다.')
    else:
        answer.delete()
    return redirect('{}#answer_{}'.format(
                resolve_url('articles:index', pk=answer.question.id), answer.id))


@login_required(login_url='articles:login')
def answer_vote(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user in answer.voter.all():
        answer.voter.remove(request.user)
    else:
        answer.voter.add(request.user)
    return redirect('{}#answer_{}'.format(
                resolve_url('articles:detail', pk=answer.question.id), answer.id))