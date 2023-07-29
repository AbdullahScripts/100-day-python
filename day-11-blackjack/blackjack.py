import random
import os
from art import logo
def chose_number():
    '''to chose random number from deck of cards'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)



def score_calculator(cards):
    """to calculate card results"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(user_score, computer_score):
  """to Compare to cards and return the winner"""
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    

    for i in range(2):
        user_cards.append(chose_number())
        computer_cards.append(chose_number())

    while not is_game_over:

        user_score=score_calculator(user_cards)
        com_score=score_calculator(computer_cards)

        print(f'user cards {user_cards} and score {user_score}')
        print(f'dealer first card {computer_cards[0]}')

        if user_score==0 or com_score==0 or user_score>21:
            is_game_over=True
        else:
            user_deal=input('type "y" for take another card and "n" for pass: ').lower()
            if user_deal=='n':
                is_game_over=True
            else:
                user_cards.append(chose_number())

    while com_score !=0 and com_score <17:
        computer_cards.append(chose_number())
        com_score=score_calculator(computer_cards)

    print(f'your last cards{user_cards} and score is {user_score}\n computers caeds{computer_cards} and score {com_score}')
    print(f'Result: {compare(user_score, com_score)}')
      
while input('do you want to play game y or n: ').lower() =='y':
   os.system('cls||clear')
   play_game()


