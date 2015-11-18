# BINARY search
# numbers in the list are in order --> 
# so, it can be possible to search an certain element, by algorithm, whose complexity ~ O(log(n/2))

list = [2,5,7,9,10,12,13,15,17,21]
x = int(input("Please enter a searched number: "))
i = 0
j = len(list)
m = int(j/2)
while list[m] != x and i < j:
	if x > list[m]:
		i = m+1
	else:
		j = m-1
		m = int((i+j)/2)
		
		print(list)
		if i > j:
			print('Элемент не найден')
		else:
			print('Индекс элемента: ', x, " [", m,"]")

			input("Press the enter key to exit...")
