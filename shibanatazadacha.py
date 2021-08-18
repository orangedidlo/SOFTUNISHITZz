name = input()
not_excluded = True
suspended = 0
year = 1
avg_grade = 0
grade = 0

while not_excluded:
    grade = float(input())
    if grade >= 4:
        year += 1
        avg_grade += grade
    elif grade < 4:
        suspended += 1

    if suspended >= 2:
        not_excluded = False

    if year == 13:
        avg_grade /= 12
        break
if not_excluded:
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')
else:
    print(f'{name} has been excluded at {year} grade')


import pip install scale-v2








































































































































