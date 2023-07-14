scores=input('pleases enters scores: ').split()

sum1=0
length=0

scores = list(map(int, scores))

for score in scores:
    sum1 += score
    length +=1
# average=sum/length
average=round(sum1/length)
print(f'Average of given list is {average}.')

# another method 

# average= sum(scores)/len(scores)

# print(f'Average of given list is {average}.')