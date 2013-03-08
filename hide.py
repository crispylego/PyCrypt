def encrypt(msg, key):
	msgList = list(msg) # message entered by user to encrypt
	keyList = list(key) # key entered by user to encrypt with
	
	while len(keyList) < len(msgList):
		keyList += keyList # while length of key is shorter than length of message, doubles key
	
	while len(keyList) > len(msgList):
		keyList.pop() # shortens key 1 character at a time until it's length = that of the message

	outList = [0] * len(msgList) # declares and initializes encrypted output list the length of the message list

	i = 0
	while i <= len(msgList) - 1:
		outList[i] = ord(msgList[i]) ^ ord(keyList[i]) # character at [i] in output list equals XOR of message[i] in dec and key[i] in dec
		outList[i] = str(hex(outList[i]).lstrip('0x')) # number at [i] converted to hex, stripped of '0x' prefix, and converted to string
		if len(outList[i]) == 1:
			outList[i] = '0' + outList[i] # if string only 1 character, add '0' in front
		elif len(outList[i]) == 0:
			outList[i] = '00' # if string empty, set it to '00'
		i+=1

	i = 0
	encrypted = ''
	while i <= len(outList) - 1:
		encrypted += outList[i] # encrypted output = 1st encrypted character + 2nd ecnrypted character + ...
		i+=1

	return encrypted

def decrypt(msg, key):
	msgList = [msg[i:i+2] for i in range(0, len(msg), 2)] # splits encrypted message into a list, each string 2 characters long
	keyList = list(key)
	
	while len(keyList) < len(msgList):
		keyList += keyList # while length of key is shorter than length of message, doubles key
	
	while len(keyList) > len(msgList):
		keyList.pop() # shortens key 1 character at a time until its length = that of the message
	
	i = 0
	while i <= len(msgList) - 1:
		msgList[i] = int(msgList[i], base=16) ^ ord(keyList[i]) # msgList[i] = msgList[i] converted to base 10 XOR dec form of keyList[i]
		msgList[i] = chr(msgList[i]) # msgList[i] converted from int to string
		i+=1
	
	i = 0
	decrypted = ''
	while i <= len(msgList) - 1:
		decrypted += msgList[i] # decrypted output = 1st decrypted character + 2nd decrypted character + ...
		i+=1
	
	return decrypted
	