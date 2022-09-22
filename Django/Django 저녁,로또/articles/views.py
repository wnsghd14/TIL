from django.shortcuts import render
import random


# Create your views here.
def todaydinner(request):
  menuitems = ['삼겹살', '소고기', '볶음밥', '샐러드', '짜장면', '햄버거', '치킨', '비빔밥', '김밥']
  
  menuimgs = [
    'https://watermark.lovepik.com/photo/20211208/large/lovepik-japanese-style-grilled-pork-belly-picture_501605503.jpg',
    'https://media.istockphoto.com/photos/sliced-tenderloin-meat-roast-beef-and-carving-set-picture-id842865316?k=20&m=842865316&s=612x612&w=0&h=G5HVOv_e0QDyI5zXH-SxSr0FrziQCJUwdICHDy7Am-o=',
    'https://recipe1.ezmember.co.kr/cache/recipe/2016/09/08/97211dec5be68c09c36e600e08485e021.jpg',
    'https://health.chosun.com/site/data/img_dir/2021/05/06/2021050601029_0.jpg',
    'https://recipe1.ezmember.co.kr/cache/recipe/2020/06/04/d96e1e81ecc8d86c922d486ec6eec4da1.jpg',
    'http://www.thekpm.com/news/photo/202201/106072_86332_1730.jpg',
    'https://t1.daumcdn.net/cfile/tistory/2403BA485896A5C829',
    'https://static.wtable.co.kr/image-resize/production/service/recipe/582/16x9/a587ba43-a6ee-482d-a3ed-8ea0dba90e7f.jpg',
    'https://recipe1.ezmember.co.kr/cache/recipe/2016/06/29/e7401296033ab8e4297cd53d71e1bba91.jpg'
  ]
  menu = list(zip(menuitems,menuimgs))
  a,b = random.choice(menu)

  context = {
  'menuitem' : a,
  'menuimg' : b,
  }
  return render(request,'todaydinner.html',context)

lottonum1 = (sorted(random.sample(range(1,46),6)))
lottonum2 = (sorted(random.sample(range(1,46),6)))
lottonum3 = (sorted(random.sample(range(1,46),6)))
lottonum4 = (sorted(random.sample(range(1,46),6)))
lottonum5 = (sorted(random.sample(range(1,46),6)))

same = []
winning = [3, 11, 15, 29, 35, 44]
winner1 = ''
winner2 = ''
winner3 = ''
winner4 = ''
winner5 = ''
for i in lottonum1:
  if i in winning:
    same.append(i)
if len(same) < 3:
  winner1='당첨X'
if len(same) == 3:
  winner1='5th'
if len(same) == 4:
  winner1='4th'
if len(same) == 5:
  winner1='3rd'
if len(same) == 6:
  if 10 in same:
    winner1='2nd'
  winner1='1st'

for i in lottonum2:
  if i in winning:
    same.append(i)
if len(same) < 3:
  winner2='당첨X'
if len(same) == 3:
  winner2='5th'
if len(same) == 4:
  winner2='4th'
if len(same) == 5:
  winner2='3rd'
if len(same) == 6:
  if 10 in same:
    winner2='2nd'
  winner2='1st'

for i in lottonum3:
  if i in winning:
    same.append(i)
if len(same) < 3:
  winner3='당첨X'
if len(same) == 3:
  winner3='5th'
if len(same) == 4:
  winner3='4th'
if len(same) == 5:
  winner3='3rd'
if len(same) == 6:
  if 10 in same:
    winner3='2nd'
  winner3='1st'

for i in lottonum4:
  if i in winning:
    same.append(i)
if len(same) < 3:
  winner4='당첨X'
if len(same) == 3:
  winner4='5th'
if len(same) == 4:
  winner4='4th'
if len(same) == 5:
  winner4='3rd'
if len(same) == 6:
  if 10 in same:
    winner4='2nd'
  winner4='1st'

for i in lottonum5:
  if i in winning:
    same.append(i)
if len(same) < 3:
  winner5='당첨X'
if len(same) == 3:
  winner5='5th'
if len(same) == 4:
  winner5='4th'
if len(same) == 5:
  winner5='3rd'
if len(same) == 6:
  if 10 in same:
    winner5='2nd'
  winner5='1st'
def lotto(request):
  context1 = {
    'winning' : winning,
    'lottonum1' : lottonum1,
    'lottonum2' : lottonum2,
    'lottonum3' : lottonum3,
    'lottonum4' : lottonum4,
    'lottonum5' : lottonum5,
    'winner1' : winner1,
    'winner2' : winner2,
    'winner3' : winner3,
    'winner4' : winner4,
    'winner5' : winner5,
  }
  return render(request, 'lotto.html',context1)
