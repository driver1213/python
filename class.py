# import pickle

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

# small exercises_wednesday
# list1 = [2, 2, 2, 2]
# sum = sum(list1)
# print(sum)

# list2 = [2, 4, 1, 7, 3]
# list2.sort()
# print(list2[-1])

# list3 = [21, 32, 2, 44, 9]
# list3.sort()
# print(list3[0])

# list4 = [10, 21, 4, 45, 66, 93]
# for number in list4:
#     if number % 2 == 0:
#         print(number, end = " ")

# list5 = [6, 4, 8, 2, -5,]
# for number in list5:
#     if number > 0:
#         print(number)

# list6 = [21, -32, 2, 44, -9]
# new_list = []
# for number in list6:
#     if number > 0:



#functions

# myVar = 1 #creating a variable with value of 2 and placing it in memory
# myVar2 = 2 #same is myVar
# def greeting(): # placing it in memory
#     print("hello world")  #placing it in execution context

# # if (myVar == 1):
#     print("Hello")
# greeting()


# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print("Shu")
# print("Thomas")
# print("Gustavo")
# print("Alim")

# def print_students():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_students()



# def greeting(person):
#     print(f'hello {person}')

# greeting('Kazim')  # will print "hello Kazim"


# def add(num1, num2):
#     sum = num1 + num2
#     return sum
# result = add (4,5)
# print(result)

# def concat_lists(list1, list2):
#     concat = list1 +list2
#     return concat

# c_result = concat_lists([1, 4, 6], [7, 9, 0])
# print(c_result)

# def cal_avg(param1, param2, param3, param4):
#     sum = param1 + param2 +param3 + param4
#     avg = sum / 4
#     return avg
# result = cal_avg()
# print(result)
# print(cal_avg())

# def sum(input):
#     sum = 0
#     for num in input:
#         sum += num
#     return sum / len(input)

# print(sum([5, 5, 5, 5, 6]))


# def myFunction(num1, num2, num3):

#     return num1*2, num2*3, num3*4  #tuple

# one, two, three = myFunction(4, 7, 9)  #destructuring
# print(one)
# print(two)
# print(three)


# def dance():
#     kind = "silly"
#     print("I am doing a %s dance" % kind)
# dance()
# print(kind)  #kind is outside of the scope so it will not print



# TAX_RATE = .09  # 9 percent tax  global memory
# COST_PER_SMALL_WIDGET = 5.00  #global memory
# COST_PER_LARGE_WIDGET = 8.00  #global memory

# def calculateCost(nSmallWidgets, nLargeWidgets):
#     subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
#     taxAmount = subTotal * TAX_RATE
#     totalCost = subTotal + taxAmount
#     return totalCost

# total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
# print('Total for first order is', total1)
# total2 = calculateCost(12, 15)
# print('Total for second order is', total2)




# def madlib(name, subject):
#     print(name + " favorite subject is " + subject + ".")
# madlib("Jean's", "math")
# madlib("Michelle's", "music")


# my_dictionary = {
#     "hello" : "world",  #if two keys are the same, it will print the last value in order
#     #"hello" : "hello1"  
#     "square_if_2" : 4,
#     0 : 1
# }

# print(my_dictionary)  #prints the whole dictionary 

#print(my_dictionary["hello"])

#print(my_dictionary.get(0))   #used to find the value of a key is there

# is_it_there = "world" in my_dictionary  #used to find if a key is there
# print(is_it_there)


# keys = my_dictionary.keys()  #gets all the keys of a dictionary
# for key in keys:
#     print(f'{key} : {my_dictionary[key]}')   #it gives all the keys


# values_list = my_dictionary.values()  #get all the values in a dictionary
# print(values_list)
# for val in values_list:   #it gives all the values 
#     if val == 4:
#         print("values found")


# for key, value in my_dictionary.items():  #destructuring
#     print(f'{key} : {value}')


# contacts = [{
#     "first name" : "Diego",
#     "last name" : "Rivera",
#     "phone" : {
#         "home" : "333-333-3333",
#         "cell" : "444-444-4444"
#     }
#     }, 
#     {
#         "first name" : "John",
#         "last name" : "Kearney", 
#     }, 
#     {
#         "first name" : "Sean",
#         "last name" : "Page"
#     }]
# print(contacts[0])



# contact = {
#     "Diego" : "222-222-2222",
#     "Foorkan" : "123-333-4444",
#     "Jean" : "777-777-7777"
# }



# phonebook = int(input("""1.Look up an entry, 2. Set an entry, 3. Delete an entry, 
# 4. List all entries, 5. Quit. What do you want to do (1-5)?
# """))
# what_entry = input("Entry: ")

# for name in contact:
#     contact[]
#     if what_entry == 1:
#         entry = contact[0]
#         print(entry)

#  Check if the user has pressed 1
#  Get search term
#  Loop the phonebook
#  use search term to find entry
#  print entry



#week 2:Tuesday

# class Greeting:
#     def say_hello(self):
#         print('hello')

# newGreetingobj = Greeting()   #the way that we create an object
# newGreetingobj.say_hello()


# class Student:
#     def __init__(self, name, lname): #__init__ is a constructor. self and name are parameters
#         self.name = name   #called an instance variable
#         self.laname = lname

    # def say_good_morning(self):  #self is a pointer, pointing back to memory object
    #     print('good morning')    

# Alina = Student()   #this creates the object first. called instantiating
# Alina.say_good_morning()

# Sean = Student()
# Sean.say_good_morning()

# Alex = Student()
# Alex.say_good_morning()

# Alina = Student("Alina")  #going into the constructor
# print(Alina.name)
# Sean = Student("Sean")
# print(Sean.name)
# Alex = Student("Alex")
# print(Alex.name)





# class Animal:
#     def __init__(self, name):
#         self.name = name

# dog = Animal("dog")
# cat = Animal("cat")
# horse = Animal("horse")

# print(dog.name)
# print(cat.name)
# print(horse.name)




# import datetime  #use this for date objects

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year

#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
            
#         return age


# sammy = Person('Sammy', 'kry', datetime.date(1998, 8, 21), '123 sesame street', 'sammy@gmail.com')
# # print(sammy.fname)  #or all in one line: print(f'{sammy.fname} {sammy.lname}')
# # print(sammy.lname)
# print(f'{sammy.fname} {sammy.lname}')

# age = sammy.age()
# print(age)


# def greeting(name):
#     count = 0
#     print(f"hello {name}")
#     count += 1
#     print(count)

# greeting("Daniela")
# greeting("Alex")
# greeting("John")
# greeting("Meryem")

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0

#     def greeting(self):
#         print(f"hello {self.name}")
#         self.count += 1

#     def printCount(self):
#         print(self.count)

# alina = Person("alina")
# print(alina.name)
# alina.greeting()
# alina.printCount()


# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0
#   def greet (self):
#     self._greet()
#   def _greet (self):
#     self.count += 1
#     if self.count > 1:
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print("Hello", self.name)
#   def __reset_count(self):
#     self.count = 0

# alex = Person("alex")
# alex._greet()
# alex.greet()



# class VString(str):  #we inherited methods from str class

#     def reverse(self, name):
        
#         rstring = ""
#         for char in name:
#             rstring = char + rstring

#         return rstring

# myString = VString("hello")

# print(myString.capitalize())  #capitalize method works because it's in the string class. 
# reversed = myString.reverse("hello")
# print(reversed)


# class Character:
#     def __init__(self, name, power, health):
#         self.name = name
#         self.power = power
#         self.health = health

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health)

# alina = Hero("pink gun", "alina", 3, 10)
# print(f'{alina.health} {alina.name} {alina.power}')
