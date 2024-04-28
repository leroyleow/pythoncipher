#caesarCipherv2 take both plaintext and key as input to create a ciphertext
# key can be more than SYMBOL by 1 round time 
import pyperclip


inputtext = input("What is input plaintext:")
key = int(input("What is the caesar key:"))     #try to convert string to
mode = input("encrypt/decrypt:")

# isDigit(key)

# Every possible symbol that can encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz!@#$%^&*()_+0123456789'

outtext = ""

for character in inputtext: 
    if character in SYMBOLS:
        #replace character by the key position
        if mode == 'encrypt':
            index = SYMBOLS.find(character) + key
        elif mode == 'decrypt':
            index = SYMBOLS.find(character) - key

        #print("the %s" % (index))

        if index >= len(SYMBOLS):
            index = index - len(SYMBOLS)
        elif index < 0:
            index = index + len(SYMBOLS)

        outtext = outtext + SYMBOLS[index]
    else:
        outtext = outtext + character

print(outtext)
pyperclip.copy(outtext)

