dust = int(input())

if dust >= 150:
    if dust > 300:
        print('실외활동을 자제하세요')
    print('미세먼지 매우나쁨')

elif dust >= 81:
    print('미세먼지 나쁨')

elif dust >= 31:
    print('미세먼지 보통')

else :
    if dust < 0:
        print('잘못된 정보입니다.')
    else:
        print('미세먼지 좋음')
    