my_name = input("What is your name? ")
my_age = int (input("What is your age? "))

print(f"My name is {my_name} and I am {my_age} years old")

first_number = int(input("Enter a number "))
second_number = int(input("Enter another number "))
operation = input("Put the operation you want ")

if operation == "+":
  print(f"The answer to you operation {first_number + second_number}")
elif operation == "-":
  print(f"The answer to you operation {first_number - second_number}")
elif operation == "*":
  print(f"The answer to you operation {first_number * second_number}")
elif operation == "/":
  print(f"The answer to you operation {first_number / second_number}")
else:
  print("The operation is not valid")

bus_capacity = 21
people_inbus= int (input("How many people are in the bus? "))
empty_seats = bus_capacity - people_inbus

if empty_seats < people_inbus:
  print (f"there  is room for more people, there is {empty_seats} left")
elif empty_seats == people_inbus:
  print(f"The bus is full, there is {empty_seats} left")
else:
  print(f"Too many people!!")
