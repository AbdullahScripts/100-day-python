print('Wellcome to Labayik Pizza Shop \n')

size=input('what size of pizza do you want \n press s , m , l,: ')

toping=input('Do you want peporoni? y / n ')

chees=input('Do you want extra Chees? y/n ')

bill=0

if size=='s':
    bill=15
elif size=='m':
    bill=20
elif size=='l':
    bill=25
else:
    print('please enter rite character ')

if toping=='y':
    bill+=2
if chees =='y':
    bill+=1
print(f'your total bill is {bill}')








