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
	for i in v:
		if st in i:
			r.append(i)

	if r:
		return r
	else:
		return ['Nothing Found']

def get_all():
	with open('notes.json', 'r') as handle:
		s = json.load(handle)

	v = list(s.values())
	a = """"""
	for i in v:
		a += i 
		a += '\n\n'
	return a

#print(note_searcher('test'))

#print(get_all())