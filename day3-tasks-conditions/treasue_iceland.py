print('wellcome to Treasure IceLand game')

path=input('where do you want to go \n left or right (l or r): ')

if path=='r':
    print('game is over!')
else:
    swimOrWait=input('do you want to swip or wait?\n s or w: ')
    if swimOrWait=='s':
        print('game is over!')
    else:
        door=input('in which door do you want to go?\n green blue or yellow \n g,b,y: ')
        if door=='g':
            print('game is over!')
        elif door=='b':
            print('game is over!')
        else:
            print('Congractulation You win')