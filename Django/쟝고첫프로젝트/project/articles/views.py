from django.shortcuts import render
from random import randint, choice
# Create your views here.
def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # name = request.GET.get('ball')
    # context = {'name' : name}
    return render(request, 'pong.html', context={'ball' : request.GET.get('ball')})

def idol(request):
    return render(request, 'idol.html')

def idolmatch(request):
    random_num = randint(0, 100)
    name = request.GET.get('name')
    if name == '':
        name = request.GET.get('idol')
    print(name)
    context = {
        'num' : random_num,
        'name' : name,
        'me' : request.GET.get('me')
    }
    return render(request, 'idolmatch.html', context)

def is_odd_even(request, number):
    result = '짝수'
    if number % 2 == 1:
        result = '홀수'
    context = {
        'num' : number,
        'result' : result
    }
    return render(request, 'is_odd_even.html', context)

def calculate(request, n1, n2):
    context = {
        'n1' : n1,
        'n2' : n2,
        'plus' : n1 + n2,
        'minus' : n1 - n2,
        'mult' : n1 * n2,
        'divide' : n1 // n2
    }
    return render(request, 'calculate.html', context)

def lorem(request):
    return render(request, 'lorem.html')

def lorem_result(request):
    text_lst = ['딸기','바나나','포도','키위','수박','레몬','귤','오렌지','파인애플','사과','복숭아']
    texts = []
    n1 = int(request.GET.get('n1'))
    n2 = int(request.GET.get('n2'))
    for _ in range(n1):
        text_part = ''
        for _ in range(n2):
            text_part += choice(text_lst)
            text_part += " "
        texts.append(text_part)
    context = {
        'n1' : n1, 
        'n2' : n2,
        'texts' : texts
    }
    return render(request, 'lorem_result.html', context)