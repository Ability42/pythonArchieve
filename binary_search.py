# BINARY search
# numbers in the list are in order --> 
# so, it can be possible to search an certain element, by algorithm, whose complexity ~ O(log(n/2))

list = [2,5,7,9,10]

print(list)
xs = int(input("Please enter a number: "))
list_min = 0
list_max = len(list)
list_mid = int(list_max/2)


while xs < list_max :
	if xs == list_mid:
		break
	elif xs < list[list_mid]:
		list_min = list_mid - 1
	else:
		list_max = list_mid + 1
	
	list_mid = int((list_max + list_min)/2)

print('A number ', xs, 'has index: ',list_mid)	

input("Press the enter key to exit...")
