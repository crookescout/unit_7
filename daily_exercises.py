# # Scout Crooke, 11/06/19, This program works on unit 7 daily exercises
#
# # exercise 1
#
# original = "abcdefghij"
# first = original[0:4]
# last = original[4:]
# final = first + last
#
# print(final)
#
# # exercise 2
#
# word = "Python"
# for x in word:
#     print(x)
#
# # exercise 3
#
#
# def without_end(the_word):
#     the_word = the_word[1:-1]
#     return the_word
#
#
# print(without_end("Hello"))
# print(without_end("python"))
# print(without_end("coding"))
#
# # exercise 4
#
#
# def longest_word(list_words):
#     longest = ""
#     for x in list_words:
#         if len(x) > len(longest):
#             longest = x
#     return longest
#
#
# print(longest_word(["hi", "this", "is", "a", "python", "code"]))
#
# # exercise 5
#
#
# def cases(words):
#     print(words.upper())
#     print(words.lower())
#
# words = input("What word(s) do you want to use?")
#
# cases(words)

# # exercise 6
#
#
# def title_case():
#     sentence = input("Give me a sentence:")
#     your_list = sentence.split(" ")
#     new_list = []
#     for your_word in your_list:
#         title_your_word = your_word[0].upper() + your_word[1:]
#         new_list.append(title_your_word)
#     phrase = " ".join(new_list)
#     return phrase
#
#
# print(title_case())


# exercise 7

#
# def replace_four(sentence):
#     your_list = sentence.split(" ")
#     new_list = []
#     for word in your_list:
#         if len(word) == 4:
#             word = "#$%@"
#             new_list.append(word)
#         else:
#             new_list.append(word)
#     phrase = " ".join(new_list)
#     return phrase
#
#
# print(replace_four("put the bags in the cars and then do them in the pool"))

# exercise 8

def bubble_sort(names):
    for x in range(len(names) -1):
        swaps = 0
        if names[x] > names[x +1]:
            temp = names[x + 1]
            names[x + 1] = names[x]
            names[x] = temp
            swaps += 1
    return names


print(bubble_sort([5, 1, 4, 2, 8]))
