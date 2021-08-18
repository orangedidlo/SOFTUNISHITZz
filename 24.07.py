# for i in range(1, 101):
#     print(i)
#
#
#
#
#

# num = int(input())
#
# for i in range(1, num + 1, 3):
#     print(i)
#
#
#
#

# num = int(input())
#
# for i in range(0, num + 1, 2):
#     print(2 ** i)
#
#
#
#
#
#
#

# num = int(input())
#
# for i in range(num, 0, -1):
#     print(i)
#
#
#
#

# symbols = input()
#
# for i in symbols:
#     print(i)
#
#
#
#

# word = input()
# score = 0
#
# for i in word:
#     if i == 'a':
#         score += 1
#     elif i == 'e':
#         score += 2
#     elif i == 'i':
#         score += 3
#     elif i == 'o':
#         score += 4
#     elif i == 'u':
#         score += 5
#
# print(score)
#
#
#
#
#
#
#


# numbers = int(input())
# sum_num = 0
#
# for i in range(numbers):
#     num = int(input())
#     sum_num += num
#
# print(sum_num)
#
#
#
#
#


# import sys
#
# num = int(input())
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for i in range(num):
#     number = int(input())
#     if number > max_number:
#         max_number = number
#     if number < min_number:
#         min_number = number
#
# print(f'Max number: {max_number}')
# print(f'Min number: {min_number}')
#
#
#
#
#
#
#

# sequences = int(input())
#
# left_sum = 0
# right_sum = 0
#
# for i in range(sequences):
#     left_num = int(input())
#     left_sum += left_num
#
# for j in range(sequences):
#     right_num = int(input())
#     right_sum += right_num
#
# diff = abs(left_sum - right_sum)
#
# if left_sum == right_sum:
#     print(f'Yes, sum = {left_sum}')
# else:
#     print(f'No, diff = {diff}')
#
#
#
#
#
#
#

# all_numbers = int(input())
# even_sum = 0
# odd_sum = 0
#
# for i in range(all_numbers):
#     number = int(input())
#
#     if i % 2 == 0:
#         even_sum += number
#     else:
#         odd_sum += number
#
# if even_sum == odd_sum:
#     print('Yes')
#     print(f'Sum = {even_sum}')
# else:
#     print('No')
#     print(f'Diff = {abs(even_sum - odd_sum)}')
#
#
#
#
#
#

# lilly_age = int(input())
# laundry_m = float(input())
# price_toy = int(input())
# total_savings = 0
# odd_bday = 0
#
# for i in range(1, lilly_age + 1):
#     if i % 2 == 0:
#         total_savings += (i * 10 / 2) - 1
#     else:
#         odd_bday = price_toy * i
#
# total_savings += odd_bday
# diff = abs(total_savings - laundry_m)
# if total_savings >= laundry_m:
#     print(f'Yes! {diff:.2f}')
# elif total_savings < laundry_m:
#     print(f'No! {diff:.2f}')








































































































































































