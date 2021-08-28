# simple rot_13 with built in python library function

import codecs

plaintext = str(input('enter plaintext: ', ))
ciphertext = codecs.encode(plaintext, 'rot_13')

print('ciphertext: ', ciphertext)
