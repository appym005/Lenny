import json
with open('notes.json', 'r') as handle:
	s = json.load(handle)

v = list(s.values())
for i in v:
	d = list(i.keys())[0]
	if 'appypro' in d:
		print(d)
		print()
		print(i[d])
		exit()
	if 'appypro' in i[d]:
		print(d)
		print()
		print(i[d])
		exit()

print('NO')

