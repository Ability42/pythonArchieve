# Написать программу поиска самого длинного слова в строке, разделенной пробелами.

def search_in_line(line):
	fin = line.split(" ")
	max_word = ""
	for word in fin:
		if len(word) >= len(max_word):
			max_word = word
	print(max_word)


def main():
	search_in_line("dwwd fdh u sud cds classsssye, this is cool--ds- --s=d-= -$% nam")


main()
input("\n\nPress the enter key to quit.")