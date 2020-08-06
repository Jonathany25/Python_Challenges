def cipher(text, shift):
    res = ""
    for i in range(0, len(text)):
        letter = text[i]

        # 65 -> A
        if letter.isupper():
            res += chr((ord(letter) + shift - 65) % 26 + 65)

        # 97 -> a
        elif letter.islower():
            res += chr((ord(letter) + shift - 97) % 26 + 97)
        else:
            res +=  letter
    return res


sentence = input("Write a sentence to apply Caesar Cipher: \n")
sint = input("Type a positive integer to shift it by (1-25): ")
s = 0

sint = int(sint)

state = input("Encrypt or decrypt: ")

if state.lower() != "encrypt" and state.lower() != "decrypt":
    print("\nEnter a valid input!")
    state = input("Encrypt or decrypt: ")

if state == "decrypt":
    s = 26 - sint
elif state == "encrypt":
    s = sint

ciphered = cipher(sentence, s)
print(ciphered)
