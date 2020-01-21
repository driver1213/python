#1
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print(f'Hello {other_person.name}, I am {self.name}!')

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f'{sonny.name} {sonny.email} {sonny.phone}')
# print(f'{jordan.name} {jordan.email} {jordan.phone}')


#2 Add a method
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print(f'{self.year} {self.make} {self.model}')

# car = Vehicle("VW", "Passat", "2015")
# car.print_info()

#3 Add a method 2
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def print_contact_info(self):
#         print(f'{self.name} {self.email} {self.phone}')

# sonny = Person("Sonny", "Sonny's email: sonny@hotmail.com", "Sonny's phone number: 483-485-4948")
# sonny.print_contact_info()


#4 Friend instance variable
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []


# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))
# print(len(sonny.friends))

#5
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []

#     def add_friend(self, friend):
#         self.friends.append(friend)

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# print(len(jordan.friends))
# jordan.add_friend(sonny)
# print(len(jordan.friends))


#6
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []

#     def num_friends(self, friend):
#         self.friends.append(friend)

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# jordan.num_friends(sonny)
# print(len(jordan.friends))


#7
class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.greeting_count = 0

    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')
        self.greeting_count += 1

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
sonny.greet(jordan)


print(sonny.greeting_count)
