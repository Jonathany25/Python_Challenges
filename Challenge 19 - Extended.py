import random as r

def cipher(text, seed, action):
    res = ""
    for i in range(0, len(text)):
        letter = text[i]
        asciiLetter = ord(letter)
        r.seed(seed)
        sinit = int(r.random() * 10)

        if action.lower() == "encrypt":
            shift = (sinit%26)
        else:
            shift = 26 - (sinit%26)

        # 65 -> A
        if letter.isupper():
            res += chr((asciiLetter + shift - 65) % 26 + 65)

        # 97 -> a
        elif letter.islower():
            res += chr((asciiLetter + shift - 97) % 26 + 97)

        else:
            res += letter
    return res


sentence = input("Write a sentence to apply Caesar Cipher: \n")
seed= input("Write the seed: ")

state = input("Encrypt or decrypt: ")

if state.lower() != "encrypt" and state.lower() != "decrypt":
    print("\nEnter a valid input!")
    state = input("Encrypt or decrypt: ")


ciphered = cipher(sentence, seed, state)
print(ciphered)
