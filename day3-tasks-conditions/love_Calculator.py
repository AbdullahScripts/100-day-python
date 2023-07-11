print('Wellcome to my Love Calculator')

yourName=input('please enter your name: ')
loverName=input("\n please enter your love one's name: ")

bothName= yourName + loverName

lowerName=bothName.lower()

t=0
r=0
u=0
e=0
l=0
o=0
v=0
e=0

t=lowerName.count('t')
r=lowerName.count('r')
u=lowerName.count('u')
e=lowerName.count('e')
l=lowerName.count('l')
o=lowerName.count('o')
v=lowerName.count('v')
e=lowerName.count('e')

true=t+r+u+e
love=l+o+v+e

score= str(true) + str(love)

# applying conditions 

condition_score=int(score)

if condition_score<10 or condition_score>90:
    print(f'your score is {score}% \nyou are like coke and mentos')
elif condition_score >= 40 and  condition_score <= 50 :
    print(f'your score is {score}% \nyou Both are so lovely')
else:
    print(f'your score is {score}% \n Best of luck')