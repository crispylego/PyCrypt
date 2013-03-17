import PyCrypt

print '\nENCRYPT\n======='
msg = raw_input('Message to encrypt: ')
key = raw_input('Key to encrypt message with: ')
print PyCrypt.encrypt(msg, key)

raw_input('')