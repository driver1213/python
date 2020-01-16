#1
# a = [1, 2, 3]
# b = [10, 20, 30]
# new_list = []
# for index in range(len(a)):
#     new_number = a[index] * b[index]
#     new_list.append(new_number)
#     #print(new_number)
# print(new_list)
#for each item in list
#make a new number equal to the first items in each list multiplied together
#add the new number to our new list
#print a new list

#2
# a = [[2, 4], [1, 6]]
# b = [[4, 7], [2, 3]]

# new_big_list = []
# for indexOne in range(len(a)):
#     #a[index] b[index]
#     #[2,4]      [4,7]
#     new_small_list = []
#     for indexTwo in range(len(a[indexOne])):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)

#3
# a = [[2, 4, 9], [1, 6, 8]]
# b = [[4, 7, 3], [2, 3, 4]]

# new_big_list = []
# for indexOne in range(len(a)):
#     #a[index] b[index]
#     #[2,4]      [4,7]
#     new_small_list = []
#     for indexTwo in range(len(a[indexOne])):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)

#4
# myList = [1, 2, 3, 4, 2, 5]
# newList = []
# for number in myList:
#     if number not in newList:
#         newList.append(number)
# print(newList)

#5
# marquez = """One Hundred Years of Solitude tells the story of the rise and fall, 
# birth and death of the mythical town of Macondo through the history of the Buendía family."""
# marq_upper = marquez.upper()
# marq_list = list(marq_upper)
# leet_marquez = []

# leet = {"A"	: "4", "E" : "3", "G" : "6", "I" : "1", "O" : "0", "S" : "5", "T" : "7"}
# for letter in marq_upper:
#     if letter in leet:
#         letter = leet[letter]
#         leet_marquez.append(letter)
#     else:
#         leet_marquez.append(letter)
# final = "".join(leet_marquez).lower()
# print(final)

#6
# word = input("What is your word? >>")
# word_lower = word.lower()
# my_list = list(word_lower)
# long_word = []

# long_vowels = {"aa" : "aaaaa", "ee" : "eeeee", "ii" : "iiiii", "oo" : "ooooo", "uu" : "uuuuu"}
# for letter in word_lower:
#     if letter in long_vowels:
#         letter = long_vowels[letter]
#         long_word.append(letter)
#     else:
#         long_word.append(letter)
# final = ''.join(long_word)
# print(final)



#7
# def caesar_encrypt(realText, step):
# 	outText = []
# 	cryptText = []
	
# 	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# 	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 	for eachLetter in realText:
# 		if eachLetter in uppercase:
# 			index = uppercase.index(eachLetter)
# 			crypting = (index + step) % 26
# 			cryptText.append(crypting)
# 			newLetter = uppercase[crypting]
# 			outText.append(newLetter)
# 		elif eachLetter in lowercase:
# 			index = lowercase.index(eachLetter)
# 			crypting = (index + step) % 26
# 			cryptText.append(crypting)
# 			newLetter = lowercase[crypting]
# 			outText.append(newLetter)
# 	return outText

# code = caesar_encrypt('abc', 2)
# print()
# print(code)
# print()
