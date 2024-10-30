#while loops = execute some code WHILE some condition remains true

#iteration - loops
#infinite loops - if it doesnt stop
# name = input("Enter your name: ")



# while name == "":
#     print("You did not enter your name.")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# age = int(input("Enter your age: "))



# while age < 0:
#     print("Age cannot be negative.")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")



# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter antoher food you like (q to quit): ")

# print("Bye!")



# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid.")
#     num = int(input("Enter a number between 1 - 10: "))

# print(f"Your number is {num}")

#for loops = execute a block of code a fixed number of times
#You can iterate over a range, string, sequence, etc.

# for x in range(1, 11): #first number is inclusive, the last number is exclusive
#     print(x)


# for x in reversed(range(1, 11)): #first number is inclusive, the last number is exclusive
#     print(x)
# print("Happy New Year!")

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue #continue skips over it
#     else:
#         print(x)


# for x in range(1, 21):
#     if x == 13:
#         break #break or return stops it before the value appears 
#     else:
#         print(x)



#Challenge

# list_of_names = ['John', 'Paul', 'George', 'Ringo']

# for name in list_of_names:
#     if name == 'George': #name can be anything x, banana, cool
#         print('George was found!')
#     else:
#         print('George was not found!')
#         print(name)

# list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']

# for name in list_of_names2:
#     if name == 'Ironman':
#         continue
#     print(name)

# for name in list_of_names2:
#     if name == 'Thor':
#         name = 'Shang-Chi'
#     print(name)

