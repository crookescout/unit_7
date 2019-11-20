# Scout Crooke, 11/11/19, this code encodes and decodes the user's word

alphabet = "abcdefghijklmnopqrstuvwxyz"


def shifted():
    """
    This function ask the user how many times they want to shift the alphabet and then shifts the alphabet
    that many times.
    Ex. shift of 3 would give
    defghijklmnopqrstuvwxyzabc
    :return: the shifted alphabet
    """
    shift = int(input("How many times do you want to shift the alphabet?"))
    first = alphabet[0:shift]
    last = alphabet[shift:]
    final = last + first
    return final


def encode(new_alphabet):
    """
    This function gets a word from the user that they want to encode and encodes the word using the alphabet and
    the shifted alphabet
    :param new_alphabet: the shifted alphabet
    :return: none
    """
    code_word = ""
    word = (input("what word do you want to encode?"))
    word = word.lower()
    for x in word:
        if x not in new_alphabet:
            code_word += x
        else:
            position = alphabet.index(x)  # this finds the index of each letter
            new_position = new_alphabet[position]  # this finds the letter of the index in the new alphabet
            code_word += new_position  # this adds the new letters from the shifter alphabet to the code word
    print("your encoded word is", code_word)


def decode(new_alphabet):
    """
    This function takes a word from the user that they want to decode and decodes the word using the alphabet and
    the shifted alphabet
    :param new_alphabet: the shifted alphabet
    :return: none
    """
    decoded_word = ""
    user_decode_word = input("what word do you want to decode?")
    user_decode_word = user_decode_word.lower()
    for x in user_decode_word:
        if x not in new_alphabet:
            decoded_word += x
        else:
            position = new_alphabet.index(x)  # this finds the index of the letter in the shifted alphabet
            new_position = alphabet[position]  # this finds the letter of the position in the real alphabet
            decoded_word += new_position  # this adds the new letter form the original alphabet to the decoded word
    print("your decoded word is", decoded_word)


def main():
    while True:
        ask = input("Press e to encode, d to decode, or q to quit")
        if ask == "e":
            new_alphabet = shifted()
            encode(new_alphabet)
        elif ask == "d":
            new_alphabet = shifted()
            decode(new_alphabet)
        elif ask == "q":
            print("See you later!")
            break


main()

