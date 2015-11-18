# INSERTION_SORT
import profile

def insert_sort(ulist):
	for j in range(1,len(ulist)):
		key = ulist[j]
		i = j
		while i>0 and ulist[i-1]<key: #reverse <key :)
			ulist[i] = ulist[i-1]
			i = i - 1
		ulist[i] = key

	print(ulist)
	return None

def main():
	ulist = [15,28,11,14,16,17]
	insert_sort(ulist)

profile.run('main()')
input("\n\nPress the enter key to exit...") 
