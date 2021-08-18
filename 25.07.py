# for num in range(1,1001):
#     if num % 10 == 7:
#         print(num)
#     else:
#         pass
#
#
#
#

# import sys
# num = int(input())
# max_num = -sys.maxsize
# sum_num = 0
#
# for i in range(num):
#     number = int(input())
#     sum_num += number
#     if number > max_num:
#         max_num = number
#
# sum_num -= max_num
#
# if max_num == sum_num:
#     print('Yes')
#     print(f'Sum = {sum_num}')
# elif max_num != sum_num:
#     diff = abs(max_num - sum_num)
#     print('No')
#     print(f'Diff = {diff}')
#
# #
#
#
#


# import sys
# num = int(input())
# odd_sum = 0
# even_sum = 0
# odd_min = sys.maxsize
# odd_max = -sys.maxsize
# even_min = sys.maxsize
# even_max = -sys.maxsize
#
# for i in range(1, num + 1):
#     number = float(input())
#
#     if i % 2 == 0:
#         even_sum += number
#         if number > even_max:
#             even_max = number
#         elif number < even_min:
#             even_min = number
#
#     else:
#         odd_sum += number
#         if number > odd_max:
#             odd_max = number
#         elif number < odd_min:
#             odd_min = number
# if odd_sum != 0 or even_sum != 0:
#     print(f'OddSum={odd_sum:.2f},')
#     print(f'OddMin={odd_min:.2f},')
#     print(f'OddMax={odd_max:.2f},')
#     print(f'EvenSum={even_sum:.2f},')
#     print(f'EvenMin={even_min:.2f},')
#     print(f'EvenMax={even_max:.2f}')
# elif odd_sum == 0 or even_sum == 0:
#     print(f'OddSum={odd_sum:.2f},')
#     odd_min = 0
#     print(f'OddMin=No,')
#     odd_max = 0
#     print(f'OddMax=No,')
#     print(f'EvenSum={even_sum:.2f},')
#     even_min = 0
#     print(f'EvenMin=No,')
#     even_max = 0
#     print(f'EvenMax=No')
#
#
#
#
#
#


# num = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
#
# for i in range(num):
#     current_number = int(input())
#     if current_number < 200:
#         p1 += 1
#
#     elif 200 <= current_number <= 399:
#         p2 += 1
#
#     elif 400 <= current_number <= 599:
#         p3 += 1
#
#     elif 600 <= current_number <= 799:
#         p4 += 1
#
#     elif current_number >= 800:
#         p5 += 1
#
# p1 /= num / 100
# p2 /= num / 100
# p3 /= num / 100
# p4 /= num / 100
# p5 /= num / 100
#
# print(f'{p1:.2f}%')
# print(f'{p2:.2f}%')
# print(f'{p3:.2f}%')
# print(f'{p4:.2f}%')
# print(f'{p5:.2f}%')
#
#
#
#


# number_in_range = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
#
# for i in range(number_in_range):
#     current_num = int(input())
#     if current_num % 2 == 0:
#         p1 += 1
#     if current_num % 3 == 0:
#         p2 += 1
#     if current_num % 4 == 0:
#         p3 += 1
#
# p1 /= number_in_range / 100
# p2 /= number_in_range / 100
# p3 /= number_in_range / 100
#
# print(f'{p1:.2f}%')
# print(f'{p2:.2f}%')
# print(f'{p3:.2f}%')
#
#
#
#


# tabs_open = int(input())
# salary = int(input())
#
# for i in range(tabs_open):
#     website = input()
#     if website == 'Facebook':
#         salary -= 150
#     elif website == 'Instagram':
#         salary -= 100
#     elif website == 'Reddit':
#         salary -= 50
#
#     if salary <= 0:
#         print('You have lost your salary.')
#         break
#
# if salary > 0:
#     print(salary)
#
#
#
#





























































































