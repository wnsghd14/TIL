T = input()
happy = T.count(":-)")
sad = T.count(":-(")
if happy<sad:
    print('sad')
elif happy>sad:
    print('happy')
elif happy == 0 and sad == 0:
    print('none')
elif happy == sad :
    print('unsure')