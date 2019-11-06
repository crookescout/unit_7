# Scout Crooke, 11/06/19, This program works on unit 7 daily exercises

# exercise 1

original = "abcdefghij"
first = original[0:4]
last = original[4:]
final = first + last

print(final)

# exercise 2

word = "Python"
for x in word:
    print(x)

# exercise 3

def without_end(the_word):
    the_word = the_word[1:-1]
    return the_word


print(without_end("Hello"))
print(without_end("python"))
print(without_end("coding"))

# exercise 4


def longest_word(list_words):
    longest = ""
    for x in list_words:
        if len(x) > len(longest):
            longest = x
    return longest


longest_word("hi", "this", "is", "a", "python", "code")

