# (habr 1.3)
# multiplication table
print("This program show multiplication table [M*a=X]...[M*b=Y]")

m = int(input("Enter M:"))
a = int(input("Enter a:"))
b = int(input("Enter b:"))

for multi in range(a,b+1):
	print("\t",multi,"*",m,"=", multi*m)

input("\n\nPress the enter key to exit.")
