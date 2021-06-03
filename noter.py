import json
import random

def noter(n):
	with open('notes.json', 'r') as handle:
		s = json.load(handle)

	n_k = int(list(s.keys())[-1])+1
	n_i = {n_k:n}

	s.update(n_i)
	with open('notes.json', 'w') as handle:
		json.dump(s, handle, indent=4)

for i in range(1000):
	title = ''
	body = ''
	for i in range(random.randint(0, 100)):
		title += chr(ord('a')+random.randint(0, 25))*random.randint(1, 3)

	for i in range(random.randint(0, 1000)):
		body += chr(ord('a')+random.randint(0, 26))*random.randint(1, 10)

	n = {title:body}
	noter(n)



