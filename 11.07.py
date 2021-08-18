# import math
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
# time_all = time_first + time_second + time_third
# minutes = time_all / 60
# seconds = time_all % 60
# minutes = math.floor(minutes)
#
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")


# number = int(input())
# bonus = 0
#
# if number <= 100:
#     bonus = 5
# elif number > 100 and number <= 1000:
#     bonus = number * 0.2
# else:
#     bonus = number * 0.1
#
# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2
#
# print(bonus)
# print(number + bonus)


# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# elif speed > 10 and speed <=50:
#     print("average")
# elif speed > 50 and speed <= 150:
#     print("fast")
# elif speed > 150 and speed <= 1000:
#     print("ultra fast")
# else:
#     print("extremely fast")


# number = float(input())
# convert_from = input()
# convert_to = input()
#
# if convert_from == "m":
#     if convert_to == "cm":
#         number *= 100
#     elif convert_to == "mm":
#         number *= 1000
# elif convert_from == "cm":
#     if convert_to == "m":
#         number /= 100
#     elif convert_to == "mm":
#         number *= 10
# elif convert_from == "mm":
#     if convert_to == "cm":
#         number /= 10
#     elif convert_to == "m":
#         number /= 1000
#
# print(f'{number:.3f}')


# hours = int(input())
# minutes = int(input()) + 15
#
# if minutes > 59:
#     hours += 1
#     minutes -= 60
# if hours > 23:
#     hours = 0
#
# print(f'{hours}:{minutes:02d}')


# budget = float(input())
# number_of_extras = int(input())
# price_of_clothes_per_1_extra = float(input())
#
# price_decor = budget * 0.1
# price_clothes = number_of_extras * price_of_clothes_per_1_extra
# if number_of_extras >= 150:
#     price_clothes -= price_clothes * 0.1
#
# total_costs = price_decor + price_clothes
#
# if total_costs > budget:
#     needed = total_costs - budget
#     print(f'Not enough money!')
#     print(f'Wingard needs {needed:.2f} leva more.')
# elif total_costs <= budget:
#     left = budget - total_costs
#     print("Action!")
#     print(f'Wingard starts filming with {left:.2f} leva left.')


# import math
#
# current_record = float(input())
# distance = float(input())
# time_for_1_meter = float(input())
#
# total_time = distance * time_for_1_meter
# additional_time = math.floor(distance / 15) * 12.5
# total_time += additional_time
#
# if total_time < current_record:
#     print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
# elif total_time >= current_record:
#     needed = total_time - current_record
#     print(f'No, he failed! He was {needed:.2f} seconds slower.')

# # USED TO TURN LINKS INTO QRCODES TO BE FOLLOWED
# import pyqrcode
# import png
# from pyqrcode import QRCode
# qr_url = "#link in question"
# url = pyqrcode.create(qr_url)
# url.png('my_qrcode.png' scale=8)

















































































