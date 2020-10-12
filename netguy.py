from duckduckpy import query

def search(s):
	
	response = query(s, container='dict')
	res = []
	for i in response['related_topics']:
		try:
			res.append(i['text'])
		except:
			pass

	return res

print(search(input()))
print()




