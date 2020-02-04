# import pickle
# import os.path

# contacts = {
#     "Diego" : "222-222-2222",
#     "Foorkan" : "123-333-4444",
#     "Jean" : "777-777-7777"
# }

# if os.path.isfile('contacts.pickle'):
#     with open('contacts.pickle', 'rb') as file_handler:
#         contacts = pickle.load(file_handler)
# else:
#     with open('contacts.pickle', 'wb') as file_handler:
#         pickle.dump(contacts, file_handler)



# print(contacts)


def print_menu():
    print('1. List all entries')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. Lookup an entry')
    print('5. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers: ")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Set an entry: ")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Delete an entry: ")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Lookup an entry: ")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()