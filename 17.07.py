# day = int(input())
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Error")


# day = input()
# if day == "Monday":
#     print("Working day")
# elif day == "Tuesday":
#     print("Working day")
# elif day == "Wednesday":
#     print("Working day")
# elif day == "Thursday":
#     print("Working day")
# elif day == "Friday":
#     print("Working day")
# elif day == "Saturday":
#     print("Weekend")
# elif day == "Sunday":
#     print("Weekend")
# else:
#     print("Error")


# animal = input()
# if animal == 'dog':
#     print('mammal')
# elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
#     print('reptile')
# else:
#     print('unknown')


# age = float(input())
# gender = input()
#
# if gender == 'm':
#     if age >= 16:
#         print('Mr.')
#     elif age < 16:
#         print('Master')
# elif gender == 'f':
#     if age >= 16:
#         print('Ms.')
#     elif age < 16:
#         print('Miss')


# product = input()
# city = input()
# quantity = float(input())
# price = 0
#
# if city == 'Sofia':
#     if product == 'coffee':
#         price = 0.5 * quantity
#     elif product == 'water':
#         price = 0.8 * quantity
#     elif product == 'beer':
#         price = 1.2 * quantity
#     elif product == 'sweets':
#         price = 1.45 * quantity
#     elif product == 'peanuts':
#         price = 1.6 * quantity
# elif city == 'Plovdiv':
#     if product == 'coffee':
#         price = 0.4 * quantity
#     elif product == 'water':
#         price = 0.7 * quantity
#     elif product == 'beer':
#         price = 1.15 * quantity
#     elif product == 'sweets':
#         price = 1.3 * quantity
#     elif product == 'peanuts':
#         price = 1.5 * quantity
# elif city == 'Varna':
#     if product == 'coffee':
#         price = 0.45 * quantity
#     elif product == 'water':
#         price = 0.7 * quantity
#     elif product == 'beer':
#         price = 1.1 * quantity
#     elif product == 'sweets':
#         price = 1.35 * quantity
#     elif product == 'peanuts':
#         price = 1.55 * quantity
#
# print(price)


# number = int(input())
#
# if -100 <= number <= 100 and number != 0:
#     print('Yes')
# else:
#     print('No')


# hours = int(input())
# days = input()
#
# if 10 <= hours <= 18:
#     if days == 'Monday' or days == 'Tuesday' or days == 'Wednesday' or days == 'Thursday' or days == \
#             'Friday' or days == 'Saturday':
#         print('open')
#     else:
#         print('closed')
# else:
#     print('closed')



# day_of_week = input()
# price = 0
# if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Friday':
#     price = 12
# elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
#     price = 14
# elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
#     price = 16
# print(price)


# product = input()
# if product in "banana, apple, kiwi, cherry, lemon, grapes":
#     print('fruit')
# elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
#     print('vegetable')
# else:
#     print('unknown')


# num = int(input())
# if 100 <= num <= 200 or num == 0:
#     pass
# else:
#     print('invalid')


# fruit = input()
# day_of_week = input()
# quantity = float(input())
# price = 0
# if day_of_week in 'Monday, Tuesday, Wednesday, Thursday, Friday':
#     if fruit == 'banana':
#         price = 2.5 * quantity
#     elif fruit == 'apple':
#         price = 1.2 * quantity
#     elif fruit == 'orange':
#         price = 0.85 * quantity
#     elif fruit == 'grapefruit':
#         price = 1.45 * quantity
#     elif fruit == 'kiwi':
#         price = 2.7 * quantity
#     elif fruit == 'pineapple':
#         price = 5.5 * quantity
#     elif fruit == 'grapes':
#         price = 3.85 * quantity
# elif day_of_week in 'Saturday, Sunday':
#     if fruit == 'banana':
#         price = 2.7 * quantity
#     elif fruit == 'apple':
#         price = 1.25 * quantity
#     elif fruit == 'orange':
#         price = 0.9 * quantity
#     elif fruit == 'grapefruit':
#         price = 1.6 * quantity
#     elif fruit == 'kiwi':
#         price = 3 * quantity
#     elif fruit == 'pineapple':
#         price = 5.6 * quantity
#     elif fruit == 'grapes':
#         price = 4.2 * quantity
# if day_of_week in 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday' and fruit in 'banana, apple, orange, kiwi, grapefruit, pineapple, grapes':
#     print(f'{price:.2f}')
# else:
#     print('error')



# city = input()
# sales = float(input())
# bonus = 0
#
# if city == "Sofia":
#     if 0 <= sales <= 500:
#         bonus = sales * 0.05
#     elif 500 < sales <= 1000:
#         bonus = sales * 0.07
#     elif 1000 < sales <= 10000:
#         bonus = sales * 0.08
#     elif sales > 10000:
#         bonus = sales * 0.12
# elif city == "Varna":
#     if 0 <= sales <= 500:
#         bonus = sales * 0.045
#     elif 500 < sales <= 1000:
#         bonus = sales * 0.075
#     elif 1000 < sales <= 10000:
#         bonus = sales * 0.1
#     elif sales > 10000:
#         bonus = sales * 0.13
# elif city == "Plovdiv":
#     if 0 <= sales <= 500:
#         bonus = sales * 0.055
#     elif 500 < sales <= 1000:
#         bonus = sales * 0.08
#     elif 1000 < sales <= 10000:
#         bonus = sales * 0.12
#     elif sales > 10000:
#         bonus = sales * 0.145
#
# if bonus > 0:
#     print(f'{bonus:.2f}')
# else:
#     print('error')


# days = int(input())
# type_room = input()
# rating = input()
# price = 0
# price_discount = 0
#
# if type_room == 'room for one person':
#     price_per_night = 18.00
#     price = (days - 1) * price_per_night
# elif type_room == 'apartment':
#     price_per_night = 25.00
#     if days < 10:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.3
#     elif 10 <= days <= 15:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.35
#     elif days > 15:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.50
# elif type_room == 'president apartment':
#     price_per_night = 35.00
#     if days < 10:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.1
#     elif 10 <= days <= 15:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.15
#     elif days > 15:
#         price = (days - 1) * price_per_night
#         price_discount = price * 0.20
#
# total_price = price - price_discount
#
# if rating == 'positive':
#     total_price = total_price + (total_price * 0.25)
# elif rating == 'negative':
#     total_price = total_price - (total_price * 0.1)
#
# print(f'{total_price:.2f}')



































