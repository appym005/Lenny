import hashlib
import os
import json
def decrypt(user, key, filename, pasd):
	try:

		with open('hiden/files', 'r') as handle:
			s = json.load(handle)

		if filename in s and s[filename] == hashlib.sha224(pasd.encode()).hexdigest():
			pass
		else:
			return 'No such file'
		fin = open(f'hiden/{filename}', 'rb')
		
		file = fin.read()
		fin.close()
		
		file = bytearray(file)

		for index, values in enumerate(file):
			file[index] = values ^ key

		fin = open(f'showing/{filename}', 'wb')
		
		fin.write(file)
		fin.close()

		os.remove(f'hiden/{filename}')
		with open('hiden/files', 'r') as handle:
			s = json.load(handle)

		s.pop(filename)

		with open('hiden/files', 'w') as handle:
			json.dump(s, handle, indent=4)
		
		return f'Showing at ./showing/{filename}'


	except Exception as e:
		return 'Error caught : ', e

#print(decrypt(appy,123,))