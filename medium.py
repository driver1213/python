# 1
# total = input("Total bill amount?")
# service = input("Level of service?")
# if service == "good" :
#     tip = float(total) * .2
#     print(f"tip amount: {tip}")
# elif service == "fair" :
#     tip = float(total) * .15
#     print(f"tip amount: {tip}")
# elif service == "bad" :
#     tip = float(total) * .1
#     print(f"tip amount: {tip}")
# total_amount = float(total) + tip
# print("$" + "%.2f" % total_amount)

#2
# total = input("Total bill amount?")
# service = input("Level of service?")
# people = input("Split how many ways?")
# if service == "good" :
#     tip = float(total) * .2
#     print(f"tip amount: {tip}")
# elif service == "fair" :
#     tip = float(total) * .15
#     print(f"tip amount: {tip}")
# elif service == "bad" :
#     tip = float(total) * .1
#     print(f"tip amount: {tip}")
# total_amount = float(total) + tip
# print("$" + "%.2f" % total_amount)
# print(f"Amount per person: {total_amount/float(people)}")

#3
# count = 0
# print("You have " + str(count) + " coins.")
# answer = input("Do you want another coin?")
# answer_lower = answer.lower()
# if answer_lower == "yes" :
#     new_answer = (count + 1)
#     print("You have " + str(new_answer) + " coins.")
# elif answer_lower == "no" :
#     print("Bye")

#4
# height = int(input("What is the height?"))
# width = int(input("What is the width?"))
# print("*" * width)
# for i in range(height - 2):
#     print("*" + " " * (width - 2) + "*")
# print("*" * width)



#5
# n=7
# for i in range(n):
#     print(' '*n, end=' ')
#     print('* '* (i))
#     n-=1

#6
# for i in range(1, 11):
#     for n in range(1, 11):
#         result = i * n
#         print(str(i) + " " + "x " + str(n) + str(result))