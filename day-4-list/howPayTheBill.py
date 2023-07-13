import random
names=input('please enter names\n seperated by comma ,: ')

nameArray=names.split(',')
end=len(nameArray)

number=random.randint(0,end-1)

print(f'{nameArray[number]},will pay the bill')