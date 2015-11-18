# SELECTION SORT

import profile

def select_sort(ulist):
	"""Selection sort function on python."""
	for j in range(len(ulist)-1,0,-1):
		pos_max = 0
		
		for i in range(1, j+1):
			if ulist[i]>ulist[pos_max]:
				pos_max = i
		
		tmp = ulist[j]
		ulist[j] = ulist[pos_max]
		ulist[pos_max] = tmp

	print(ulist)
	pass


def main():
	ulist = [15,28,11,14,16,17]
	select_sort(ulist)

profile.run('main()')

input("\n\nPress enter to exit...")