# for h in range(24):
#     for m in range(60):
#         print(f'{h}:{m}')
#
#
#
#


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')
#
#
#
#


# number = int(input())
# counter = 0
#
# for x1 in range(0, number + 1):
#     for x2 in range(0, number + 1):
#         for x3 in range(0, number + 1):
#             if x1 + x2 + x3 == number:
#                 counter += 1
#
# print(counter)
#
#
#
#


# initial_n = int(input())
# last_n = int(input())
# magical_n = int(input())
# combination_counter = 0
# is_found = False
#
#
# for i in range(initial_n, last_n + 1):
#     for j in range(initial_n, last_n + 1):
#         combination_counter += 1
#         if i + j == magical_n:
#             print(f'Combination N:{combination_counter} ({i} + {j} = {magical_n})')
#             is_found = True
#     if is_found:
#         break
# if not is_found:
#     print(f'{combination_counter} combinations - neither equals {magical_n}')
#
#
#
#


# savings1 = 0
# enough_money = False
#
# while True:
#     destination = input()
#     if destination == 'End':
#         break
#     budget_for_destination = float(input())
#     while True:
#         savings = float(input())
#         savings1 += savings
#         if savings1 >= budget_for_destination:
#             print(f'Going to {destination}!')
#             enough_money = True
#             savings1 = 0
#             break
#
#
#
#


# number_floors = int(input())
# number_rooms_per_floor = int(input())
#
# for i in range(number_floors, 0, -1):
#     current_floor = i * 10
#     for j in range(number_rooms_per_floor):
#         current_number_room = current_floor + j
#         if i == number_floors:
#             print(f'L{current_number_room}', end=" ")
#         elif i % 2 != 0:
#             print(f'A{current_number_room}', end=" ")
#         else:
#             print(f'O{current_number_room}', end=" ")
#     print()
#
#
#
#
#

number_tickets = 0
counter = 0
standard = 0
kid = 0
student = 0

while True:
    name_movie = input()

    if name_movie == 'Finish':
        break

    number_seats = int(input())

    while True:
        type_ticket = input()

        if type_ticket == 'End':
            break

        counter += 1
        number_tickets += 1

        if type_ticket == 'standard':
            standard += 1
        elif type_ticket == 'kid':
            kid += 1
        elif type_ticket == 'student':
            student += 1

        if counter >= number_seats:
            break

    print(f'{name_movie} - {(counter / number_seats) * 100:.2f}% full.')








































































































































































































































