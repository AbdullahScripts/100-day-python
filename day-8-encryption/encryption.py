import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

def casear(text_input,shift_position,type_process):
    final_word=''
    if type_process=='encode':
        for c in text_input:
            position=alphabet.index(c)
            position +=shift_position
            final_word+=alphabet[position]
    elif type_process=='decode':
        for c in text_input:
            position=alphabet.index(c)
            position -=shift_position
            final_word+=alphabet[position]

    print(final_word)

continue_process=True

while continue_process==True:
    
    type_of_process=input('type "encode" or "decode" according to your need: ').lower()
    word=input('enter your word: ')
    shift_nmbr=int(input('how many number to shift: '))

    casear(text_input=word,shift_position=shift_nmbr,type_process=type_of_process)

    isgoing=input('do you want to continue yes or no: ').lower()
    if isgoing=='no':
        continue_process=False






