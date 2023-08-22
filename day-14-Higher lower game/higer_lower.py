import random
import os
from data import data
from art import logo
from art import vs
def pick_person():
    return random.choice(data)

# def compare(guess,nonGuess):
def compare(choice,score):
    
    
    print(f' a:{choice["a"]["name"]} nwho is a {choice["a"]["description"]} lived in {choice["a"]["country"]} ')
    print(vs)
    print(f' b:{choice["b"]["name"]} nwho is a {choice["b"]["description"]} lived in {choice["b"]["country"]} ')
    guess=input('what is your answer: ').lower()

    if guess=='a':
        nonGuess='b'
    else:
        nonGuess='a'

    follower=choice[guess]['follower_count']
    com_follower=choice[nonGuess]['follower_count']
    if follower > com_follower:
        choice1={

        'a':choice[guess],
        'b':pick_person()

                        }
        score1= score+1
        os.system('cls||clear')
        print(f'your score is:{score1}')
        compare(choice=choice1,score=score1)

    else:
        os.system('cls||clear')
        print('Game Ended')
        print(f'your score is:{score}')

choice={

        'a':pick_person(),
        'b':pick_person()

    }

score=0

# compare(guess,nonGuess)
print(logo)
compare(choice,score)


