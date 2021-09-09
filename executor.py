import subprocess


def execute(c):
	a = list(c.split('|'))
	print(a)
	s = [i.split() for i in a]
	print(s)
	s1 = subprocess.run(s[0], universal_newlines=True, stdout=subprocess.PIPE)
	if '|' in c:
		s2 = subprocess.run(s[1], universal_newlines=True, input=s1.stdout, stdout=subprocess.PIPE)
		r = f'\nstdout:\n{s2.stdout}\n\nstderr:\n{s2.stderr}'
		print(s2.stdout)
		print(s2.stderr)
		return r
	r = f'\nstdout:\n{s1.stdout}\n\nstderr:\n{s1.stderr}'
	print(s1.stdout)
	print(s1.stderr)
	return r

#print(execute('echo hello > zxc'))