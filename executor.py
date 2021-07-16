import subprocess
import os 

def execute(c):
	s = list(c.split(' '))
	print(s)
	s = subprocess.run(s,capture_output=True)
	r = f'\nstdout:\n{s.stdout.decode()}\n\nstderr:\n{s.stderr.decode()}'
	print(s.stdout)
	print(s.stderr)
	return r

#execute('ls')