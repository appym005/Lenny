from duckduckpy import query

def search(s):

	t = ''
	for i in s:
		if (i.lower() >= 'a' and i.lower() <= 'z') or (i.lower() >= '0' and i.lower() <= '9') or i == ' ':
			t += i

	response = query(t, container='dict')
	res = []
	for i in response['related_topics']:
		try:
			res.append(i)
		except:
			pass

	result = []
	for i in res:
	    try:
	        result.append(i['text'])
	    except:
	        for j in i['topics']:
	            result.append(j['text'])

	return result

"""result = search(input())
for i in result:
	print(i)




"""