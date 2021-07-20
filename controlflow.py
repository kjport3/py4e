# # Pay Calculator
# hrs = input('Enter Hours: ')
# rate = input('Enter Rate: ')
#
# # Conditionals
# try:
#     if float(hrs) <= 0 or float(rate) <= 0:
#         print('Both numbers should be greater than zero.')
#     elif 0 < float(hrs) <= 40:
#         pay = float(hrs) * float(rate)
#         print('Pay: ' + str(pay))
#     elif float(hrs) > 40:
#         overtime_rate = input('You worked over 40 hours, qualifying you for overtime pay. Enter overtime rate: ')
#         if float(overtime_rate) <= float(rate):
#             print('Your overtime rate should be greater than your regular rate.')
#         else:
#             # Calculate Base Pay
#             pay = float(40) * float(rate)
#             print('Base Pay: ' + str(pay))
#             # Calculate Overtime Pay
#             overtime_hrs = float(hrs) - 40
#             overtime_pay = float(overtime_hrs) * float(overtime_rate)
#             print('Overtime Pay: ' + str(overtime_pay))
#             # Calculate Total Pay
#             total_pay = float(pay) + float(overtime_pay)
#             print('Total Pay: ' + str(total_pay))
# except:
#     print('Error, please enter a numeric input.')

# # Exercise 3.1
# hrs = input('Enter Hours: ')
# rate = input('Enter Rate: ')
# try:
#     h = float(hrs)
#     r = float(rate)
# except:
#     print("Error, please enter numeric input")
#     quit()
#
# if h > 40:
#     overtime_hrs = h - 40
#     overtime_rate = r * 1.50
#     overtime_pay = overtime_rate * overtime_hrs
#     base_pay = 40 * r
#     total_pay = base_pay + overtime_pay
#     print(str(total_pay))
# else:
#     total_pay = h * r
#     print(str(total_pay))

# # Exercise 3.2
# score = input("Enter Score: ")
# try:
#     fscore = float(score)
#     if 0 < fscore < 1:
#         # Print grade
#         if fscore >= 0.9:
#             print('A')
#         elif fscore >= 0.8:
#             print('B')
#         elif fscore >= 0.7:
#             print('C')
#         elif fscore >= 0.6:
#             print('D')
#         else:
#             print('F')
#     else:
#         print('Please enter a value between 0.0 and 1.0')
# except:
#     print('Enter a number between 0.0 and 1.0')

# # Importing modules
# import math
# import random
#
# print(math)
# print(random)
#
# i = 2.2
# ceiling = math.ceil(i)
# print(ceiling)
#
# print(math.pi)
#
# x = random.randint(1, 100)
#
# print(x)

# # Exercise 4.1
# def computepay(h, r):
#     if h > 40:
#         overtime_hrs = h - 40
#         overtime_rate = r * 1.50
#         overtime_pay = overtime_rate * overtime_hrs
#         base_pay = 40 * r
#         total_pay = base_pay + overtime_pay
#         return total_pay
#     else:
#         total_pay = h * r
#         return total_pay
#
#
# hrs = input('Enter Hours: ')
# rate = input('Enter Rate: ')
# fhrs = float(hrs)
# frate = float(rate)
#
# p = computepay(fhrs, frate)
# print("Pay ", p)

# Exercise 5.1
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        fnum = int(num) if num else None
        if largest is None or int(num) > int(largest):
            largest = num
        elif smallest is None or int(num) < int(smallest):
            smallest = num
    except:
        print("Invalid input")

print("Maximum is " + str(largest))
print("Minimum is " + str(smallest))

# Reverse string traversal
fruit = 'apple'
index = -1
print(fruit[:])
while True:
    if index == -(len(fruit) + 1):
        break
    letter = fruit[index]
    print(letter)
    index = index - 1








