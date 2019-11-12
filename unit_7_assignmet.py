# Scout Crooke, 11/11/19, this code encodes and decodes the user's word

alphabet = "abcdefghijklmnopqrstuvwxyz"
ask = input("Press e to encode, d to decode, or q to quit")


def shifted():
    shift = int(input("How many times do you want to shift the alphabet?"))
    first = alphabet[0:shift]
    last = alphabet[shift:]
    final = last + first
    return final


def encode(new_alphabet):
    word = (input("what word do you want to encode?"))
    word = word.lower()
    code_word = " "
    for x in word:
        position = alphabet.index(x)
        new_position = new_alphabet[position]
        print("your encoded word is", new_position)


def main():
    new_alphabet = shifted()
    encode(new_alphabet)


main()

