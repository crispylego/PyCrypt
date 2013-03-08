import hide

print '\nDECRYPT\n======='
msg = raw_input('Message to decrypt: ')
key = raw_input('Key to decrypt message with: ')
print hide.decrypt(msg, key)

raw_input(' ')