import random

rules='''
wellcome to my Game game rules are:

1: Rock beats scissors and loses to paper. 

2: Paper beats rock, but loses to scissors. 

3: Scissors beat paper but loses to rock. 

'''
print(rules)

seassor='''
        ________
    ____'   ____)_____
               _______)
            ___________)
            (______)
    ----.___(____)

'''
rock='''
    __________
----'    _____)
        (______)
        (______)
        (_____)
----.____(____)

'''

papper='''
    __________
----'    _____)____
            _______)
            _________)
          __________)
-----.___________)

'''
computer=str(random.randint(0,2))

user=input('\nEnter 0 for rock ,1 for papper ,2 for seassor: ')

if user=='0':
    if computer=='0':
        print(f'\nyou chose: rock\n {rock}\n computer chose: rock\n{rock}\n match ties 🧐')
    elif computer=='1':
        print(f'\nyou chose: rock\n {rock}\n computer chose:papper\n{papper}\n You lose 😭')
    else:
        print(f'\nyou chose: rock\n {rock}\n computer chose: seassor\n{seassor}\n You won 😍')
elif user=='1':
    if computer=='0':
        print(f'\nyou chose: papper\n {papper}\n computer chose: rock\n{rock}\n you won 😍')
    elif computer=='1':
        print(f'\nyou chose: papper\n {papper}\n computer chose:papper\n{papper}\n Match ties 🧐')
    else:
        print(f'\nyou chose: papper\n {papper}\n computer chose: seassor\n{seassor}\n you lose 😭')
elif user=='2':
    if computer=='0':
        print(f'\nyou chose: seassor\n {seassor}\n computer chose: rock\n{rock}\n you lose 😭')
    elif computer=='1':
        print(f'\nyou chose: seassor\n {seassor}\n computer chose:papper\n{papper}\n you won 😍')
    else:
        print(f'\nyou chose: seassor\n {seassor}\n computer chose: seassor\n{seassor}\n match ties 🧐')
else:
    print('please enter right number')
