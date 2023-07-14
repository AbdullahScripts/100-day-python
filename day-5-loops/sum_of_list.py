scores=input('pleases enters scores: ').split()

sum=0

scores = list(map(int, scores))

for score in scores:
    sum += score
print(f'sum of given list is {sum}.')
