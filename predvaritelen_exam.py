# 02.BRACELET STAND
#
#
#
# pocket_money = float(input())
# earnings_per_day = float(input())
# expenses_total = float(input())
# price_gift = float(input())
# days_left = 5
# total_earnings = 0
# total = 0
# pocket = 0
#
# for i in range(days_left):
#     total_earnings += earnings_per_day
#     pocket += pocket_money
#
# total_earnings += pocket
# total = (total_earnings - expenses_total)
#
# if total >= price_gift:
#     print(f'Profit: {total:.2f} BGN, the gift has been purchased.')
# elif price_gift > total:
#     needed = price_gift - total
#     print(f'Insufficient money: {needed:.2f} BGN.')
#
#
#

# 03.EXCURSION CALCULATOR
# number_people = int(input())
# season = input()
# price = 0
#
# if number_people <= 5:
#     if season == 'spring':
#         price = number_people * 50
#     elif season == 'summer':
#         price = number_people * 48.50
#     elif season == 'autumn':
#         price = number_people * 60
#     elif season == 'winter':
#         price = number_people * 86
# elif number_people > 5:
#     if season == 'spring':
#         price = number_people * 48
#     elif season == 'summer':
#         price = number_people * 45
#     elif season == 'autumn':
#         price = number_people * 49.50
#     elif season == 'winter':
#         price = number_people * 85
#
# if season == 'summer':
#     price -= price * 0.15
# elif season == 'winter':
#     price += price * 0.08
#
# print(f'{price:.2f} leva.')


# 01.CAT DIET

# maznini_gr = 0
#
#
# mazini_percent = int(input())
# proteini_percentage = int(input())
# vuglehidrati_percentage = int(input())
# calories_total = int(input())
# h2o_percentage = int(input())
#
# mazini_gr = (mazini_percent * calories_total) / 9
# proteini_gr = (proteini_percentage * calories_total) / 4
# vuglehidrati_gr = (vuglehidrati_percentage * calories_total) / 4
#
# total_food_weight = mazini_gr + proteini_gr + vuglehidrati_gr
# calories_per_gr = calories_total / total_food_weight
#
# non_h20_percentage = 100 - h2o_percentage
# calories = (calories_per_gr * non_h20_percentage)
#
# print(f'{calories:.4f}')
#
#
#


# 06.MULTIPLICATION TABLE

# #number = input()
# number1 = number[2]
# number2 = number[1]
# number3 = number[0]
# number = int(number)
# number1 = int(number1)
# number2 = int(number2)
# number3 = int(number3)
#
# for i in range(number1 + 1, 0, -1)):
#     for j in range(number2 + 1, 0, -1)):
#         for t in range(number3 + 1, 0, -1):
#             print(f'{number1} * {number2} * {number3} = {number1 * number2 * number3};')
#
#


# number_students = int(input())
# total_score = 0
# dvoikari = 0
# troikari = 0
# chetvorki = 0
# otlichnici = 0
#
# for i in range(1, number_students + 1):
#     score_exam = float(input())
#     total_score += score_exam
#     if score_exam <= 2.99:
#         dvoikari += 1
#     elif 3 <= score_exam <= 3.99:
#         troikari += 1
#     elif 4 <= score_exam <= 4.99:
#         chetvorki += 1
#     elif score_exam >= 5:
#         otlichnici += 1
#
# fail_percent = (dvoikari / number_students) * 100
# troika_percent = (troikari / number_students) * 100
# chetvorka_percent = (chetvorki / number_students) * 100
# otlichni_percent = (otlichnici / number_students) * 100
# average = total_score / number_students
#
# print(f'Top students: {otlichni_percent:.2f}%')
# print(f'Between 4.00 and 4.99: {chetvorka_percent:.2f}%')
# print(f'Between 3.00 and 3.99: {troika_percent:.2f}%')
# print(f'Fail: {fail_percent:.2f}%')
# print(f'Average: {average:.2f}')


# 05.SALES FOR FKN EXCURSIONS

# excursions_sea = int(input())
# excursions_mountain = int(input())
# profit = 0
#
#
# while True:
#     package_choice = input()
#     if package_choice == 'Stop':
#         break
#
#     if package_choice == 'sea':
#         if excursions_sea == 0:
#             continue
#         profit += 680
#         excursions_sea -= 1
#
#     elif package_choice == 'mountain':
#         if excursions_mountain == 0:
#             continue
#         profit += 499
#         excursions_mountain -= 1
#
#     if excursions_mountain == 0 and excursions_sea == 0:
#         break
#
#
#
# if excursions_mountain == 0 and excursions_sea == 0:
#     print('Good job! Everything is sold.')
# else:
#     print(f'Profit: {profit} leva.')
#


#

#
# number = int(input())
#
# for x1 in range(number):
#     for x2 in range(number):
#         for x3 in range(number):
#             print(f'{x3} * {x2} * {x1} = {x1 * x2 * x3};')


# number = int(input())
# first_digit = number % 10
# second_digit = number // 10 % 10
# third_digit = number // 100 % 10
#
# for x1 in range(1, first_digit + 1):
#     for x2 in range(1, second_digit + 1):
#         for x3 in range(1, third_digit + 1):
#             print(f'{x1} * {x2} * {x3} = {x1 * x2 * x3};')






# excursions_sea = int(input())
# excursions_mountain = int(input())
# profit = 0
# sea_counter = 0
# mountain_counter = 0
#
# while excursions_mountain == 0 and excursions_sea == 0:
#     package_choice = input()
#     if package_choice == 'Stop':
#         break
#
#     if package_choice == 'sea':
#         excursions_sea -= 1
#         sea_counter += 1
#         if excursions_sea == 0:
#             continue
#         else:
#             profit += 680
#
#     elif package_choice == 'mountain':
#         excursions_mountain -= 1
#         mountain_counter += 1
#         if excursions_mountain == 0:
#             continue
#         else:
#             profit += 499
#
#
# if excursions_mountain == mountain_counter and excursions_sea == sea_counter:
#     print('Good job! Everything is sold.')
# else:
#     print(f'Profit: {profit} leva.')







# seaside_number = int(input())
# mountain_number = int(input())
# profit = 0
#
# while seaside_number == 0 and mountain_number == 0:
#     type_trip = input()
#     if type_trip == 'Stop':
#         break
#
#     if type_trip == 'sea':
#         if seaside_number > 0:
#             profit += 680
#             seaside_number -= 1
#     elif type_trip == 'mountain':
#         if mountain_number > 0:
#             profit += 499
#             mountain_number -= 1
#
# if seaside_number == 0 and mountain_number == 0:
#     print("Good job! Everything is sold.")
# print(f'Profit: {profit} leva.')























































