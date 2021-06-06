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

	return 'Noted'

def note_searcher(st):
	with open('notes.json', 'r') as handle:
		s = json.load(handle)

	v = list(s.values())
	r = []
	for i in range(1,len(v)):
		if st in v[i]:
			r.append((i,v[i]))

	if r:
		return r
	else:
		return ['Nothing Found']

def get_all():
	with open('notes.json', 'r') as handle:
		s = json.load(handle)

	v = list(s.values())
	k = list(s.keys())
	a = """\n"""
	for i in range(1,len(v)):
		a += k[i] + ': ' + v[i] 
		a += '\n\n'
	return a

def delete(n):
	with open('notes.json', 'r') as handle:
		s = json.load(handle)

	if n > len(s):
		return 'Not found'
			
	for i in range(n, len(s) - 1):
		s[str(i)] = s[str(i+1)]

	s.popitem()

	with open('notes.json', 'w') as handle:
		json.dump(s, handle, indent=4)

	return 'Deleted'



#print(note_searcher('test'))

#print(get_all())

#print(delete(8))