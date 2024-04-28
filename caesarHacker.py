#Caesar Cipher Hacker

cipherText= 'guv6Kv6Kz!K6rp5r7Kzr66ntr.'
# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?'

for key in range(len(SYMBOLS)):
    translated=''

    for symbol in cipherText:
        if symbol in SYMBOLS:
            symbolindex = SYMBOLS.find(symbol)
            translatedindex = symbolindex - key

            #Handle the wrappedaround
            if translatedindex < 0:
                translatedindex = translatedindex + len(SYMBOLS)
            
            #Append the decrypted symbol
            translated = translated + SYMBOLS[translatedindex]
        else:
            # Append the symbol without encrypting/decrypting
            translated = translated + symbol
    
    #display every possible decryption
    print('Key #%s %s' %(key, translated))