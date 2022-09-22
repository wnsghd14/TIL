from multiprocessing import context
from random import random
from django.shortcuts import render
import random
# Create your views here.
def index(request):
  names = ['주세환','오진수','임수경','조병진','차화영','최근영','김선교']
  name = random.choice(names)
  context = {
    'name': name,
    'img' : 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg'
  }
  return render(request,'index.html', context)

def welcome(request,name):
  # print(name)
  context = {
    'name' : name,
    'greetings' : [
      'hi','구텐탁','오하요'
    ],
    'images' : [
      'https://byline.network/wp-content/uploads/2018/05/cat.png',
      'https://sunstat.com/wp-content/uploads/2019/01/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C-%EB%B0%B0%EA%B2%BD%EC%9D%B4%EB%AF%B8%EC%A7%80.png',
    ],
  }
  return render(request, 'welcome.html',context)