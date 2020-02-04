# class AccountHolder():
#     def __init__(self, fname, lname, mname, atype, balance, status):
#         self.firstname = fname
#         self.lastname = lname
#         self.middlename = mname
#         self.accountType = atype 
#         self.balance = balance
#         self.status = status


# class Bank():
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.accounts = []

#     def open_new_account(self, fname, lname, mname, atype, balance, status):
#         if balance >= 100 :
#             new_acc = AccountHolder(fname, lname, mname, atype, balance, status)    #create an account holder
#             self.accounts.append(new_acc)     # store new account holder in account list
#             return f"A {atype} account was created for {fname} {mname} {lname} with a balance of {balance}" #return "Account created for fname lname"
#         else:
#             return "Insufficient funds. You need $100 dollars to open an account." #return "Insufficient deposit amount"

#     def show_account_holders(self):
        
#         for account_holder_obj in self.accounts:
#             print(f'{account_holder_obj.first_name} {account_holder_obj.last_name}')

# #definition of main that included a while loop with menu of things
# def main():
#     wellsfargo = Bank("wells fargo", "123 sesame street")
#     action = 1

#     while action != 6:
#         print("1. Create an account")
#         print("2. Print list of all account holders")

#         print("6. Exit application")

#         action = int(input("Choose from the given options: "))
#         if (action == 1):
#             fname = input("What is the first name?")
#             mname = input("What is the middle name?")
#             lname = input("What is the last name?")
#             atype = input("What type of account would you like to open? Checking or saving? ")
#             deposit = int(input("How much would you like to deposit?"))
#             wellsfargo.open_new_account(fname, lname, mname, atype, deposit, "new")

#         elif (action == 2):
#             wellsfargo.show_account_holders()

#         if (action == 6):
#             break

# #main
# main()

# wellsfargo = Bank("usaa", "123 sesame street")
# wellsfargo.open_new_account("Diego", "Rivera", "NMN", "checking", 102, "new")


#!/usr/bin/env python

# Step 9: Bonus Challenge 2
# Create a zombie character that cannot die 
# and have it fight the hero instead of the goblin.

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health 
        self.power = power
        
    def alive(self):
        if self.health > 0 :
            return True 
        else: 
            return False
        
    def attack(self, enemy):
    
        if enemy.name != "zombie":
            enemy.health -= self.power
        
        if(self.name == "hero"):
            print(f"You do {self.power} damage to the {enemy.name}.")
        elif(self.name == "goblin" or self.name == "zombie" or self.name == "medic" or self.name == "shadow" or self.name == "baby_yoda" or self.name == "mando"):
            print(f"The {self.name} does {self.power} damage to you.")
        
            
    def print_status(self):
        if self.name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.name == "goblin" or self.name == "zombie":
            print(f"The {self.name} has {self.health} health and {self.power} power.")
            
            
class Hero(Character):
    def __init__(self, name, health, power):
        self.name = "Neo"
        super(Hero, self).__init__(name, health, power)
        
        
class Goblin(Character):
    def __init__(self, name, health, power):
        self.name = "goblin"
        super(Goblin, self).__init__(name, health, power)
        
class Zombie(Character):
    def __init__(self, name, health, power):
        self.name = "zombie"
        super(Zombie, self).__init__(name, health, power)

class Medic(Character):
    def __init__(self, name, health, power):
        self.name = "medic"
        super(Medic, self).__init__(name, health, power)

class Shadow(Character):
    def __init__(self, name, health, power):
        self.name = "shadow"
        super(Shadow, self).__init__(name, health, power)

class Baby_Yoda(Character):
    def __init__(self, name, health, power):
        self.name = "baby_yoda"
        super(Baby_Yoda, self).__init__(name, health, power)

class Mando(Character):
    def __init__(self, name, health, power):
        self.name = "mando"
        super(Mando, self).__init__(name, health, power)
        
hero = Hero("Neo", 10, 5)
goblin = Goblin("Goblin", 6, 2)
zombie = Zombie("Zombie", 10, 1)
medic = Medic("Medic", 10, 2)
shadow = Shadow("Shadow", 8, 2)
baby_yoda = Baby_Yoda("Baby_Yoda", 10, 4)
mando = Mando("Mando", 10, 4)

def main(enemy):
    
    while enemy.alive() > 0 and hero.alive():
        
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            enemy.attack(hero)
            if not enemy.alive():
                print(f"The {enemy.name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            
            if not hero.alive():
                print("You are dead.")

main(goblin)
main(zombie)
main(medic)
main(shadow)
main(baby_yoda)
main(mando)