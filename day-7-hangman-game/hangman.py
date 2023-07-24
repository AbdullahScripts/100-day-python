import os
# for random number 
import random
# for logo and art 
from art import stages,logo
# for array of words 
from data import word_list

# need arrays and variable 

chose=[]
loop=0
life=7

# flag variable 

end=False

chosen_word=random.choice(word_list)

# for initial characters to print 

for chr in chosen_word:
    chose+='-'
    # logo print 
print(logo)
# hint word length 
print(chose)

# main loop for guess the word 

while end==False:
        
    guess=input('please enter a single character to guess the word: ').lower()
    os.system('cls')

    for chr in chosen_word:
        loop+=1
        if chr==guess:
            chose[loop-1]=guess

# for print art if guess is not match 

    if guess not in chosen_word:
        life-=1
        print(f'{guess} is not in the word ')
        print(stages[life])

# end the game if lose 

    if life==0:
        end=True
        print(f'you lose correct word was {chosen_word}')
# end game if won 
    if '-' not in chose:
        print('You Save the man 😍')
        end=True
    # print chosen word 
    print(chose)
    loop=0
   












