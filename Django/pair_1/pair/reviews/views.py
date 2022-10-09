from django.shortcuts import render, redirect
from .models import Review 

def index(request):
  reviews = Review.objects.all()
  context = {
    'reviews' : reviews,
  }

  return render(request,'reviews/index.html', context)

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  
  Review.objects.create(
    title=title,
    content=content,
  )
  context = {
    'title': title,
    'content': content,
  }

  return render(request, 'reviews/create.html', context)

def new(request):
  
  return render(request, 'reviews/new.html')

def detail(request, pk):
  review = Review.objects.get(pk = pk)
  context = {
    'review' : review,
  }

  return render(request, 'reviews/detail.html', context)

def delete(request, pk):
  review = Review.objects.get(pk = pk)
  review.delete()
  # cnt = 0
  # while True:
  #   cnt += 1
  #   review = Review.objects.get(pk + cnt)
  #   review.pk = pk + cnt
  #   review.save()

  return redirect('reviews:index')

def edit(request, pk):
  review = Review.objects.get(pk = pk)
  context = {
    'review' : review,
  }
  
  return render(request, 'reviews/edit.html', context)

def update(request, pk):
  review = Review.objects.get(pk = pk)
  title_ = request.GET.get('title')
  content_ = request.GET.get('content')
  review.title = title_
  review.content = content_
  review.save()

  return redirect('reviews:index')
