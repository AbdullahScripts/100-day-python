import random
from art import logo
def guess_number(level,level_want,number_to_guess):
   
    chance=level[level_want]
    is_guessed=False

    while is_guessed==False:
        number=int(input('enter any number to guess: '))
        if number >number_to_guess:
            print ('please guess small number: ')
        
        
        elif number <number_to_guess:
            print('please guess large number: ')
        elif number==number_to_guess:
            is_guessed=True
            return 'you won'
            
        
        if chance==0:
            is_guessed=True
            return('you lose')
        chance -=1
        print(f'{chance} chances are remaining')
        

number_to_guess=random.randint(1,101)

print(logo)
  #Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")



level_want=input('type "easy" for easy level \nType "hard" for hard level: ').lower()

level={
    'easy':10,
    'hard':5
}


print(guess_number(level,level_want,number_to_guess))
