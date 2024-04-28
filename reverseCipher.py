#Reverse Cipher encrypts the message by printing plaintext in reverse order

plaintext = 'Three can keep a secret, if two of them are dead.'
ciphertext = ''


i = len(plaintext) - 1
while i >= 0:
    ciphertext = ciphertext + plaintext[i]
    print("i is ", i, ", plaintext[i] is ",plaintext[i],", ciphertext is ",ciphertext)
    i = i - 1

print('The encrypted string is :\n' + ciphertext)

i = len(ciphertext) - 1
plaintext = ''
while i >= 0:
    plaintext = plaintext + ciphertext[i]
    i = i - 1

print('The plaintext is :\n' + plaintext)