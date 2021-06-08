from encrypt import encrypt
from decrypt import decrypt
import json
import hashlib

def auth(user, pasd):
	with open('pwd', 'r') as f:
		s = json.load(f)

	if user in s:
		key = hashlib.sha224(pasd.encode()).hexdigest()
		if key == s[user]:
			return True
		else:
			return 'Password mismatch'
	else:
		return 'User not found'

def create_user(user, pasd):
	with open('pwd', 'r') as handle:
		s = json.load(handle)

	if user in s:
		return 'Already exists'
	else:
		n = {user: hashlib.sha224(pasd.encode()).hexdigest()}

	s.update(n)
	with open('pwd', 'w') as handle:
		json.dump(s, handle, indent=4)
	return 'Done'

def hide_file(user, pasd, path, filename):
	if auth(user, pasd) == True:
		key = hashlib.sha224((user+pasd).encode()).hexdigest()
		key = int(key, 16)%254
		return encrypt(path, key, filename, pasd)
	else:
		return auth(user, pasd)

def get_file(user, pasd, filename):
	if auth(user, pasd) == True:
		key = hashlib.sha224((user+pasd).encode()).hexdigest()
		key = int(key, 16)%254
		return decrypt(user, key, filename, pasd)
	else:
		return auth(user, pasd)


if __name__ == "__main__":
	run = True
	user = input('User?')
	pasd = input('Pasd?')
	while run:
		
		c = int(input('Action?'))
		if c == 1:
			print(create_user(user, pasd))
		elif c == 2:
			path = input('Path?')
			filename = input('Filename?')
			print(hide_file(user, pasd, path, filename))
		else:
			filename = input('Filename?')
			print(get_file(user, pasd, filename))

		run = input('More?')