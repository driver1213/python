
# print("""I'm a string
# sleejnd
# sljlekjs
# skejfj
# fjeijlije
#         """)

# print("I'm a string")
# print("skdfjlkefvngil")

#concatenating

# print("hello " + "world")

# print("""I\'m a\t\t\t\tstring
# asdlklendlkg
# \v\v\v\v
# """)

# a = 20
# b = 15
# c = 3

# print(a + b + c)

# name = "Diego"
# lname = "Rivera"

# output = "good morning {0} {1} {1} {0}".format(name, lname)

# print(output)

# student1 = "john"
# student2 = "diego"
# output = f'hello world {student1} {student2}'

# print(output)

# print(type(student1))

# test = '5'
# test1 = '5' + 5
# print(isinstance(test1, int))

# consolelog = input("Enter your name >>")
# output = f'Hello {consolelog}'
# dataType = type(consolelog)
# print(dataType)

# input_number_from_user = input("Insert a number >>")

# print(type(input_number_from_user))

# casted_output = int(input_number_from_user)

# print(type(casted_output))

# some_math = casted_output *7
# print(some_math)


# age = 26
# if True :
#     print(age)

# print(age)


# name = input("Enter in your name >>")
# if (name == "Diego"):
#     print(name)

# name = "Diego"
# age = 26

# if (age <= 25):
#     print(age)

# if (age != 25):
#     print("you are not 25")

# if (age > 25):
#     print("you are over 25")

# if age >= 21:
#     print("You get free beer")
# else:
#     print("Sorry no beer for you")

# if age >= 21:
#   print("You get free beer")
# elif age < 18:
#   print("What are you even doing here?")
# else:
#   print("Sorry no beer for you")


# greeting = "Hello {}, it is very nice to meet you and your friend {}!"
# name_of_user = input("What is your name? ")
# length_of_name = len(name_of_user)
# if length_of_name > 6:
#     name_of_friend = input("What is your friend's name? ")
#     print(greeting.format(name_of_user, name_of_friend))
# elif length_of_name > 7:
#     name_of_friend = input("What is your friend's name? ")
#     print(greeting.format(name_of_user, name_of_friend))
# else:
#     print("OK, I'll ask again some other time.")


# position matters where you put the count value
# count = 0
# while(count < 10):
    
#     count += 1
#     print("The count is ", count)


# answer = ''
# while answer != 'when':
#   answer = input('Say when: ')
#   answer = answer.lower()
# print("Cheese")

# while True:
#   answer = input('Say when: ')
#   if answer.lower() == 'when':
#     break
# print("Cheese")

# numbers = [1, 2, 3, 4, 5]
# #print(number [1])

# number_elements = len(number)
# numbers[0] =  "Monday"

# print(numbers)


# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.append("binge watch a show")
# todos.append("go to sleep")

# index = 0
# while index < len(todos):
#     print(f'{index + 1} : {todos[index]}') #if you add {index +1}it will show 1 when printed
#     index += 1

# to_do = []
# new_list = input("Add new list:")
# enter = ""
# while to_do is True:
#     print(to_do.append(new_list))
# if to_do is False:
#     print(to_do)

# list1 = []
# to_add = input("Add items to the list.")
# while len(to_add) > 0:
#     list1.extend([to_add])
#     print(list1)
#     to_add = input("Add itmes to the list ")
# print(list1)


# numbers = [1, 2, 3, 4, 5]

# new_nums = 

# mixed_list = [1, 4, 7, 2, 8]
# mixed_list.sort()
# print(mixed_list)

# count - 0 
# while count < 3:
#     print('Hello')
#     count +=1

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for variable in alphabet:
#     print("Hello") #will print Hello 26 times 
    # if you print("variable") it will print each letter in alphabet
    #if you want a determined set of values use slicing method
    #ex. number = [1,2,3,4,5,6]
    #new_list = [1:] will start at 2

# for variable in range(10):
#         square = (variable+1)*(variable+1)
#         print(square) #variale will start at 0 up to 9
# for variable in range(5, 10): #will start at 5 up to 9
# for variable in range(5,10,2): #will start at 5 increment by to 2 and stop at 9

# students = ["matt", "foorkan", "alex", "mary"]
# for variable in students:
#     print(variable) #will print matt, foorkan, alex, mary



# for outter_variable in range(3): #outer loop
#     for inner_variable in range(5): #inner loop
#         print(outter_variable, inner_variable)

# for outer in range(1, 11): #outer loop
#     for inner in range(1, 11): #inner loop
#         result = outer * inner   # here is the multiplication of outer * inner
#         print(f"{outer} x {inner} = {result}")

# list1 = ["Week1", "Week2", "Week3", "Week4", "Week5"]
# list2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# list3 = ["lessons", "exercises"]
# for i in range(len(list1)):
#     print(list1[i] + ":")
#     for x in range(len(list2)):
#         print(list2[x] + " = ") #when in doubt just start printing
#         for y in range(len(list3)):
#             print(list3[y])


