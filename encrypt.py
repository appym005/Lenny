import hashlib
import json
def encrypt(path, key, filename, pasd):
	try:
		
		with open('hiden/files', 'r') as handle:
			s = json.load(handle)

		if filename in s:
			return "filename exists"
		else:
			with open('hiden/files', 'r') as handle:
				s = json.load(handle)

			n = {filename: hashlib.sha224(pasd.encode()).hexdigest()}
			s.update(n)

			with open('hiden/files', 'w') as handle:
				json.dump(s, handle, indent=4)


		fin = open(path, 'rb')
		
		file = fin.read()
		fin.close()
		
		file = bytearray(file)

		for index, values in enumerate(file):
			file[index] = values ^ key

		fin = open(f'hiden/{filename}', 'wb')
		
		fin.write(file)
		fin.close()
		
		return 'Hiding Done...'

		
	except Exception as e:
		print(e)
		return(e)
