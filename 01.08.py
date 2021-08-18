# book_needed = input()
# counter = 0
#
# while True:
#     next_book = input()
#
#     if next_book == 'No More Books':
#         print(f'The book you search is not here!')
#         print(f'You checked {counter} books.')
#         break
#     elif next_book == book_needed:
#         print(f'You checked {counter} books and found it.')
#         break
#     else:
#         counter += 1
#
#
#

# failed_threshold = int(input())
# bad_grades_counter = 0
# name_last_problem = ''
# problem_counter = 0
# grades_sum = 0
#
# while True:
#     name_problem = input()
#     if name_problem == 'Enough':
#         break
#     grade = int(input())
#
#     if grade <= 4:
#         bad_grades_counter += 1
#
#         if bad_grades_counter >= failed_threshold:
#             break
#
#     name_last_problem = name_problem
#     problem_counter += 1
#     grades_sum += grade
#
# if bad_grades_counter < failed_threshold:
#     average_score = grades_sum / problem_counter
#     print(f'Average score: {average_score:.2f}')
#     print(f'Number of problems: {problem_counter}')
#     print(f'Last problem: {name_last_problem}')
# else:
#     print(f'You need a break, {bad_grades_counter} poor grades.')
#
#
#
#


# money_needed = float(input())
# money_available = float(input())
# day_counter = 0
# spend_counter = 0
#
#
# while money_available < money_needed and spend_counter < 5:
#
#     financial_decision = input()
#     sum_financial_decision = float(input())
#     day_counter += 1
#
#     if financial_decision == 'spend':
#         money_available -= sum_financial_decision
#         spend_counter += 1
#         if money_available < 0:
#             money_available = 0
#     elif financial_decision == 'save':
#         money_available += sum_financial_decision
#         spend_counter = 0
#
# if spend_counter == 5:
#     print("You can't save the money.")
#     print(day_counter)
# elif money_available >= money_needed:
#     print(f'You saved the money for {day_counter} days.')
#
#
#
#
#


# steps_goal = 10000
# total_steps = 0
#
# while total_steps <= steps_goal:
#     current_walk = input()
#
#     if current_walk == 'Going home':
#
#         last_walk = int(input())
#         total_steps += last_walk
#         if total_steps >= steps_goal:
#             print('Goal reached! Good job!')
#             print(f'{total_steps - steps_goal} steps over the goal!')
#             break
#         else:
#             steps_needed = steps_goal - total_steps
#             print(f'{steps_needed} more steps to reach goal.')
#             break
#     else:
#         steps = int(current_walk)
#         total_steps += steps
# else:
#     print('Goal reached! Good job!')
#     print(f'{total_steps - steps_goal} steps over the goal!')
#
#
#
#
#


# change = int(float(input()) * 100)
# number_coins = 0
#
# while change > 0:
#     number_coins += 1
#
#     if change >= 200:
#         change -= 200
#     elif change >= 100:
#         change -= 100
#     elif change >= 50:
#         change -= 50
#     elif change >= 20:
#         change -= 20
#     elif change >= 10:
#         change -= 10
#     elif change >= 5:
#         change -= 5
#     elif change >= 2:
#         change -= 2
#     elif change >= 1:
#         change -= 1
#
# print(number_coins)
#
#
#
#
#


# width = int(input())
# length = int(input())
#
# total_size = width * length
#
# while total_size > 0:
#     number_pieces = input()
#
#     if number_pieces == 'STOP':
#         break
#
#     total_size += int(number_pieces)
#
# if total_size > 0:
#     print(f'{total_size} pieces are left.')
# else:
#     print(f'No more cake left! You need {abs(total_size)} pieces more.')
#
#
#
#
#


# best_player = ''
# most_goals = 0
#
# while True:
#     player = input()
#     if player == 'END':
#         break
#     goals = int(input())
#
#     if goals > most_goals:
#         most_goals = goals
#         best_player = player
#         if goals >= 10:
#             break
#
#
# print(f'{best_player} is the best player!')
# if most_goals >= 3:
#     print(f'He has scored {most_goals} goals and made a hat-trick !!!')
# else:
#     print(f'He has scored {most_goals} goals.')
#
#
#
#
#


# bought_food_gr = int(input()) * 1000
# food_eaten_gr = 0
#
# while True:
#
#     intake_grams = input()
#
#     if intake_grams == 'Adopted':
#         break
#
#     food_eaten_gr += int(intake_grams)
#
# if bought_food_gr >= food_eaten_gr:
#     print(f'Food is enough! Leftovers: {bought_food_gr - food_eaten_gr} grams.')
# elif food_eaten_gr > bought_food_gr:
#     print(f'Food is not enough. You need {food_eaten_gr - bought_food_gr} grams more.')
#
#
#
#
#
#
















































































































































































































