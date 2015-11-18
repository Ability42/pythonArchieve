def tabulate(func, start, end, tab):
	for b in range(start, end, tab):
		print(func, "= ", b*b)

def main():
	tabulate("x*x" , -3, 7, 1)

main()
input("exit..")
