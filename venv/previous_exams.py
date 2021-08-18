#01 - 18.07.2020
# aviocompany = input()
# adult_tickets = int(input())
# kid_tickets = int(input())
# net_adult_ticket_price = float(input())
# a_for_efforts = float(input())
#
# total_kid_price = (net_adult_ticket_price * 0.3) + a_for_efforts
# total_adult = net_adult_ticket_price + a_for_efforts
#
# total_tickets = (total_adult * adult_tickets) + (total_kid_price * kid_tickets)
#
# profit = total_tickets * 0.2
#
# print(f'The profit of your agency from {aviocompany} tickets is {profit:.2f} lv.')
#
#
#


#02 - 18.07.2020
price_luggage_over_20 = float(input())
luggage_kg = float(input())
days_till_trip = int(input())
number_luggages = int(input())
price_luggage = 0

if luggage_kg < 10:
    price_luggage = price_luggage_over_20 * 0.2
elif 10 <= luggage_kg <= 20:
    price_luggage = price_luggage_over_20 / 2
elif luggage_kg > 20:
    price_luggage = price_luggage_over_20

if days_till_trip > 30:
    price_luggage += price_luggage * 0.1
elif 





























































