# words = input()
# while words != 'Stop':
#     print(words)
#     words = input()
#
#
#

# username = input()
# password = input()
# entered_password = input()
#
# while entered_password != password:
#     entered_password = input()
#
# print(f'Welcome {username}!')
#
#
#
#


# number = int(input())
# sum_num = 0
#
# while sum_num < number:
#     new_number = int(input())
#     sum_num += new_number
#
# print(sum_num)
#
#
#
#


# number = int(input())
# sequential_number = 1
#
# while sequential_number <= number:
#     print(sequential_number)
#     sequential_number = sequential_number * 2 + 1
#
#
#
#
#
#
#

# inputting = input()
# total_moneys = 0
#
# while inputting != 'NoMoreMoney':
#     number_sum = float(inputting)
#
#     if number_sum < 0:
#         print('Invalid operation!')
#         break
#     print(f'Increase: {number_sum:.2f}')
#
#     total_moneys += number_sum
#
#     inputting = input()
#
# print(f'Total: {total_moneys:.2f}')
#
#
#
#

# import sys
# command = input()
# max_number = -sys.maxsize
#
# while command != 'Stop':
#     command1 = int(command)
#
#     if command1 > max_number:
#         max_number = command1
#
#     command = input()
#
# print(max_number)
#
#
#
#

# import sys
# command = input()
# min_number = sys.maxsize
#
# while command != 'Stop':
#     command1 = int(command)
#
#     if command1 < min_number:
#         min_number = command1
#
#     command = input()
#
# print(min_number)
#
#
#
#
#
# name = input()
# not_excluded = True
# suspended = 0
# year = 1
# avg_grade = 0
# grade = 0
#
# while not_excluded:
#     grade = float(input())
#     if grade >= 4:
#         year += 1
#         avg_grade += grade
#     elif grade < 4:
#         suspended += 1
#
#     if suspended >= 2:
#         print(f'{name} has been excluded at {year} grade')
#         not_excluded = False
#
#     if year == 12:
#         avg_grade /= year
#         break
# if not_excluded == True and year == 12:
#     print(f'{name} graduated. Average grade: {avg_grade:.2f}')
#
#
#
#
#
# name = input()
# not_excluded = True
# suspended = 0
# year = 1
# avg_grade = 0
# grade = 0
#
# while not_excluded:
#     grade = float(input())
#     if grade >= 4:
#         year += 1
#         avg_grade += grade
#     elif grade < 4:
#         suspended += 1
#
#     if suspended >= 2:
#         not_excluded = False
#
#     if year == 13:
#         avg_grade /= 12
#         break
# if not_excluded:
#     print(f'{name} graduated. Average grade: {avg_grade:.2f}')
# else:
#     print(f'{name} has been excluded at {year} grade')




















