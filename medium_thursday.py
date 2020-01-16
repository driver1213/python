#1
# def smallest(list):
#     small = list[0]
#     for x in list:
#         if x < small:
#             small = x
#     return small
# print(smallest([3, 2, 11, 19, 13]))



#2
# def largest(list):
#     large = list[0]
#     for x in list:
#         if x > large:
#             large = x
#     return large
# print(largest([3, 2, 11, 19, 13]))



#3
# def shortest(strings):
#     word_len = []
#     for n in strings:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[0][1]

# print(shortest(["run", "walk", "accelerate", "study", "to"]))



#4
# def find_longest_word(words_list):
#     word_len = []
#     for n in words_list:
#         word_len.append((len(n), n))
#     word_len.sort()
#     return word_len[-1][1]

# print(find_longest_word(["run", "walk", "accelerate", "study", "to"]))