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
			res.append(i)#['text'])
		except:
			pass

	return response

print(search(input()))




