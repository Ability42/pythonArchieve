# N0D (Найбільший Спільний Дільник)
import profile

def nod(m,n):
	if m < n:
		m, n = n, m
	r = m % n
	while r != 0:
		m = n
		n = r
		r = m % n
		print(n)
	return None
		
	

def main():
	nod(2166,6099)

profile.run('main()')

input("Press the enter key to exit...")