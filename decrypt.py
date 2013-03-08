import PyCrypt

print '\nDECRYPT\n======='
msg = raw_input('Message to decrypt: ')
key = raw_input('Key to decrypt message with: ')
print PyCrypt.decrypt(msg, key)

raw_input(' ')