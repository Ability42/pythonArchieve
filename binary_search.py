# BINARY search
# numbers in the list are in order --> 
# so, it can be possible to search an certain element, by algorithm, whose complexity ~ O(log(n/2))




def bin_search(ulist, xs):
	list_min = 0
	list_max = len(ulist) - 1
	found = False


	while list_min <= list_max and not found:
		list_mid = (list_max + list_min)//2

		if xs == ulist[list_mid]:
			found = True
		else:
			if xs < ulist[list_mid]:
				list_max = list_mid - 1
			else:
				list_min = list_mid + 1

	return found

test_list = [1,4,7,8,21,42,]

print(bin_search(test_list, 1))
print(bin_search(test_list, 5))
print(bin_search(test_list, 31))
print(bin_search(test_list, 42))



input("Press the enter key to exit...")
