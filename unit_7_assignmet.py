# Scout Crooke, 11/11/19, this code encodes and decodes the user's word

alphabet = "abcdefghijklmnopqrstuvwxyz"


def shifted():
    shift = int(input("How many times do you want to shift the alphabet?"))
    first = alphabet[0:shift]
    last = alphabet[shift:]
    final = last + first
    return final


def encode(new_alphabet):
    code_word = ""
    word = (input("what word do you want to encode?"))
    word = word.lower()
    for x in word:
        if x not in new_alphabet:
            code_word += x
        else:
            position = alphabet.index(x)
            new_position = new_alphabet[position]
            code_word += new_position
    print("your encoded word is", code_word)


def decode(new_alphabet):
    decoded_word = ""
    user_decode_word = input("what word do you want to decode?")
    user_decode_word = user_decode_word.lower()
    for x in decoded_word:
        if x not in new_alphabet:
            decoded_word += x
        else:
            position = new_alphabet.index(x)
            new_position = alphabet[position]
            decoded_word += new_position
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

