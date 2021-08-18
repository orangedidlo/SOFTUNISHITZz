# type_movie = input()
# rows = int(input())
# columns = int(input())
# gainz = 0
# cinema_capacity = rows * columns
# if type_movie == 'Premiere':
#     price = 12
#     gainz = cinema_capacity * price
# elif type_movie == 'Normal':
#     price = 7.5
#     gainz = cinema_capacity * price
# elif type_movie == 'Discount':
#     price = 5
#     gainz = cinema_capacity * price
#
# print(f'{gainz:.2f} leva')


# degrees = int(input())
# time_of_day = input()
#
# if 10 <= degrees <= 18:
#     if time_of_day == 'Morning':
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif time_of_day == 'Afternoon':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif time_of_day == 'Evening':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
# elif 18 < degrees <= 24:
#     if time_of_day == 'Morning':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif time_of_day == 'Afternoon':
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     elif time_of_day == 'Evening':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
# elif degrees >= 25:
#     if time_of_day == 'Morning':
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     elif time_of_day == 'Afternoon':
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
#     elif time_of_day == 'Evening':
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")


# type_flower = input()
# num_flowers = int(input())
# budget = int(input())
# price = 0
# discount = 0
#
# if type_flower == 'Roses':
#     if num_flowers > 80:
#         discount = (num_flowers * 5) * 0.1
#         price = (num_flowers * 5) - discount
#     else:
#         price = num_flowers * 5
# elif type_flower == 'Dahlias':
#     if num_flowers > 90:
#         discount = (num_flowers * 3.8) * 0.15
#         price = (num_flowers * 3.8) - discount
#     else:
#         price = num_flowers * 3.8
# elif type_flower == 'Tulips':
#     if num_flowers > 80:
#         discount = (num_flowers * 2.8) * 0.15
#         price = (num_flowers * 2.8) - discount
#     else:
#         price = num_flowers * 2.8
# elif type_flower == 'Narcissus':
#     if num_flowers <= 120:
#         discount = (num_flowers * 3) * 0.15
#         price = (num_flowers * 3) + discount
#     else:
#         price = num_flowers * 3
# elif type_flower == 'Gladiolus':
#     if num_flowers <= 80:
#         discount = (num_flowers * 2.5) * 0.2
#         price = (num_flowers * 2.5) + discount
#     else:
#         price = num_flowers * 2.5
#
# if price <= budget:
#     left = budget - price
#     print(f'Hey, you have a great garden with {num_flowers} {type_flower} and {left:.2f} leva left.')
# elif price > budget:
#     needed = price - budget
#     print(f'Not enough money, you need {needed:.2f} leva more.')


# budget = int(input())
# season = input()
# fishermen = int(input())
# price = 0
#
# if season == 'Spring':
#     price = 3000
# elif season in 'Summer, Autumn':
#     price = 4200
# elif season == 'Winter':
#     price = 2600
#
# if fishermen <= 6:
#     price -= price * 0.1
# elif 7 < fishermen <= 11:
#     price -= price * 0.15
# elif fishermen > 12:
#     price -= price * 0.25
#
# if fishermen % 2 == 0:
#     if season == 'Autumn':
#         pass
#     else:
#         price -= price * 0.05
#
# if price <= budget:
#     left = budget - price
#     print(f'Yes! You have {left:.2f} leva left.')
# elif price > budget:
#     needed = price - budget
#     print(f'Not enough money! You need {needed:.2f} leva.')
#
#
#


# budget = float(input())
# season = input()
# destination = ''
# location = ''
# budget1 = 0
#
# if season == 'summer':
#     destination = 'Camp'
# elif season == 'winter':
#     destination = 'Hotel'
#
# if budget <= 100:
#     location = 'Bulgaria'
#     if season == 'summer':
#         budget1 = budget - (budget * 0.3)
#     elif season == 'winter':
#         budget1 = budget - (budget * 0.7)
# elif 100 < budget <= 1000:
#     location = 'Balkans'
#     if season == 'summer':
#         budget1 = budget - (budget * 0.4)
#     elif season == 'winter':
#         budget1 = budget - (budget * 0.8)
# elif budget > 1000:
#     location = 'Europe'
#     budget1 = budget - (budget * 0.9)
#
# if location == 'Europe':
#     destination = 'Hotel'
# budget2 = budget - budget1
#
# print(f'Somewhere in {location}')
# print(f"{destination} - {budget2:.2f}")
#
#
#
#
#


# N1 = int(input())
# N2 = int(input())
# operator = input()
# result = 0
#
# if operator == '+':
#     result = N1 + N2
#     if result % 2 == 0:
#         result_type = 'even'
#     else:
#         result_type = 'odd'
#     print(f'{N1} {operator} {N2} = {result} - {result_type}')
# elif operator == '-':
#     result = N1 - N2
#     if result % 2 == 0:
#         result_type = 'even'
#     else:
#         result_type = 'odd'
#     print(f'{N1} {operator} {N2} = {result} - {result_type}')
# elif operator == '*':
#     result = N1 * N2
#     if result % 2 == 0:
#         result_type = 'even'
#     else:
#         result_type = 'odd'
#     print(f'{N1} {operator} {N2} = {result} - {result_type}')
# elif operator == '/':
#     if N2 == 0:
#         print(f'Cannot divide {N1} by zero')
#     else:
#         result = N1 / N2
#         print(f'{N1} {operator} {N2} = {result:.2f}')
# elif operator == '%':
#     if N2 == 0:
#         print(f'Cannot divide {N1} by zero')
#     else:
#         result = N1 % N2
#         print(f'{N1} {operator} {N2} = {result}')
#
#
#
#
#
#
#


# month = input()
# nights = int(input())
# cost_studio = 0
# cost_apartment = 0
#
#
# if month in 'May, October':
#     cost_apartment = 65
#     cost_studio = 50
#
#     if 7 < nights <= 14:
#         cost_studio -= cost_studio * 0.05
#     elif nights > 14:
#         cost_studio -= cost_studio * 0.3
#
# elif month in 'June, September':
#     cost_apartment = 68.7
#     cost_studio = 75.2
#
#     if nights > 14:
#         cost_studio -= cost_studio * 0.2
#
# elif month in 'July, August':
#     cost_apartment = 77
#     cost_studio = 76
#
# if nights > 14:
#     cost_apartment -= cost_apartment * 0.1
#
#
# total_studio = nights * cost_studio
# total_apartment = nights * cost_apartment
#
# print(f'Apartment: {total_apartment:.2f} lv.')
# print(f'Studio: {total_studio:.2f} lv.')
#
#
#
#
#


# hour_exam = int(input())
# minute_exam = int(input())
# hour_arrival = int(input())
# minute_arrival = int(input())
#
# exam_time_minutes = (hour_exam * 60) + minute_exam
# arrival_time_minutes = (hour_arrival * 60) + minute_arrival
# diff = abs(exam_time_minutes - arrival_time_minutes)
# hour = diff // 60
# minute = diff % 60
#
# if exam_time_minutes == arrival_time_minutes:
#     print('On time')
# elif exam_time_minutes > arrival_time_minutes:
#     if diff <= 30:
#         print(f'On time')
#         print(f'{minute} minutes before the start')
#     elif 30 < diff < 60:
#         print('Early')
#         print(f'{minute} minutes before the start')
#     elif diff > 59:
#         print('Early')
#         print(f'{hour}:{minute:02d} hours before the start')
# elif arrival_time_minutes > exam_time_minutes:
#     print('Late')
#     if diff < 60:
#         print(f'{minute} minutes after the start')
#     else:
#         print(f'{hour}:{minute:02d} hours after the start')
#
#
#
#
#
#
#


# leap_normal = input()
# holidays = int(input())
# weekends = int(input())
#
# number_games = ((48 - weekends) * 3/4) + weekends + (holidays * 2/3)
# if leap_normal == 'leap':
#     number_games += number_games * 0.15
#
# print(int(number_games))
#
#
#
#
#
#









































































































