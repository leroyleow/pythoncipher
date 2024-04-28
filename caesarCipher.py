import pyperclip

#The string to be encrypted/decrypted
plaintext = "This is my secret message."
#plaintext = "guv6Kv6Kz!K6rp5r7Kzr66ntr."

#The encryption/decryption key:
key=13

#Whether the program encrypts or decrypts
mode = 'encrypt'

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?'

#Store the encrypted/decrypted form of the message
ciphertext = ''

for symbol in plaintext:
    #Note: Only symbols in the SYMBOLS can be encrypted or decrypted
    if symbol in SYMBOLS:
        if mode == 'encrypt':
            translatedindex = SYMBOLS.find(symbol) + key
        elif mode == 'decrypt':
            translatedindex = SYMBOLS.find(symbol) - key

        if translatedindex >= len(SYMBOLS):
            translatedindex = translatedindex - len(SYMBOLS)
        elif translatedindex < 0:
            translatedindex =  translatedindex + len(SYMBOLS)
            
        ciphertext = ciphertext + SYMBOLS[translatedindex]
    else:
        ciphertext = ciphertext + symbol
    
print(ciphertext)
pyperclip.copy(ciphertext)
