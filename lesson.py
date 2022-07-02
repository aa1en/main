"""1.CALCULATOR"""
# def add(x, y):
#     return x + y


# def subtract(x, y):
#     return x - y


# def multiply(x, y):
#     return x * y


# def divide(x, y):
#     return x / y


# print("Select operation. \n1)Add \n2)Subtract \n3)Multiply \n4)Divide")
# while True:
#     choice = input("Enter choice(1,2,3,4): ")
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(f'{num1} + {num2} = {add(num1, num2)}')
#         elif choice == '2':
#             print(f'{num1} - {num2} = {subtract(num1, num2)}')
#         elif choice == '3':
#             print(f'{num1} * {num2} = {multiply(num1, num2)}')
#         elif choice == '4':
#             print(f'{num1} / {num2} = {divide(num1, num2)}')
        

#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
    
#     else:
#         print("Invalid Input")

"""2.MAX NUMBER"""
# def max_number(x,y):
#     if x - y > 0:
#         return  f'{x} is max'
#     elif x - y == 0:
#         return 'Numbers are equal'
#     else:
#         return f'{y} is max'


# num1 = float(input('Enter number 1: '))
# num2 = float(input('Enter number 2: '))
# print(max_number(num1, num2))

"""3.SUM ALL NUMBERS"""

# def sum_all_numbers(x):
#     return sum(x)


# numbers_quantity = int(input('How many numbers you want to enter: '))
# my_list = []
# while True:
#     if len(my_list) == numbers_quantity:
#         break
#     else:
#         number = float(input('Enter number for sum: '))
#         my_list.append(number)
# print(sum_all_numbers(my_list))

"""4.MULTIPLY ALL NUMBERS"""

# def multiply_nums(x):
#     result = 1
#     for num in x:
#         result *= num
#     return result


# my_list = []
# number = int(input('How many numbers you want to multiply? >'))
# while True:
#     if len(my_list) == number:
#         break
#     else:
#         num_multy = int(input('Enter number for multiply: '))
#         my_list.append(num_multy)
# print(multiply_nums(my_list))

"""5.LETTER AND NUMBER"""

# def letter_nums_sum(str):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     sum = 0
#     for i in str:
#         if i in letters:
#             sum += (letters.index(i) + 1)
#         else:
#             sum += int(i)
#     return sum


# string =input('Enter text: ').lower()
# print(letter_nums_sum(string))

"""6.GET READY!"""

# def get_ready(x,y,z):
#     if x > 16 and y > 16 and z > 16:
#         return "Get ready!"
#     else:
#         return "Too young!"


# x = int(input('Enter your age: '))
# y = int(input('Enter your age: '))
# z = int(input('Enter your age: '))
# print(get_ready(x, y, z))


