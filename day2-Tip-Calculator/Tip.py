
print('helo welcome to my tip calculator')
 
amount=float(input('\n please enter your amount to pay: '))
person=int(input('\n how many persons to split bill: '))
persent=int(input('\n how many persent do you want to give tip 12,15,20,or any other: '))


persentage=amount*(1+persent/100)


tip=round(persentage/person,2)


print(f'each one have to pay {tip}$')

