#2.
# a = 1
# b = 2
# c = 3

# for c in range(3, 1000):
#     for b in range(2, c):
#         for a in range(1, b):
#             if a*a+b*b==c*c and a+b+c==1000:
#                 print(f"a = {a}, b = {b}, c = {c}")
#                 print(a*b*c)

#other solution
def checkTrip(a, b, c):
    if (a * a) + (b * b) == (c * c) :
        return True
    else:
        return False
a = 0
while a < 500:
    a += 1
    b = a + 1
    while b < 500:
        c = 1000 - (a + b)
        if checkTrip(a, b, c) == False :
            b += 1
        else:
            product = a*b*c
            print(a, b, c)
            print(product)
            break






#3.
str1=input("input string1: ")
str2=input("input string2: ")

for i in str1:
    if i not in str2:
        print(f'{i} is in str1')

    if i in str2:
        if i not in str1:
            print(f'{i} is in str2')



    #other solution
def difference(str1, str2):
    for char in str2:
        if char in str1:
            pass
        else:
            return char

print(difference("abcd", "abcde"))