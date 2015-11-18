# (habr 1.2)quadratic equation
import math

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

d = b*b - 4*a*c

if d<0:
	print("equation has a complex square\n")
else:
	#sqrtd = math.sqrt(d)

	x1 = (-b-math.sqrt(d))/(2*a)
	x2 = (-b+math.sqrt(d))/(2*a)

	print("x1 =", x1, "\tx2 =", x2)

input("\n\nPress the enter key to exit.")