import os

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]='excellent'
    elif score>80:
        student_grades[student]='Good'
    elif score>70:
        student_grades[student]='nice'
    elif score>60:
        student_grades[student]='average'
    else:
        student_grades[student]='fail'

input('what is your name: ')
os.system('cls||clear')
for student in student_grades:
    print(f'{student}:{student_grades[student]}')
    
