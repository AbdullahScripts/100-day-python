scores=input('pleases enters scores: ').split()

high_score=0

scores = list(map(int, scores))

for score in scores:
    if score>high_score:
        high_score=score
print(f'High score in given list is {high_score}.')
