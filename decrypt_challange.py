# the python chalange (http://www.pythonchallenge.com/) #1
# program is decrypt the text file by "mapping" letters "over 2"
# K --> M
# A --> C
# X --> Z
# Z --> B 

key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
line = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq  \
glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu  \
ynnjw ml rfc spj."

def encrypt(dic, string):
	stringX = list(string)
	for each in stringX:
		if each in dic:
			x = dic.index(each)
			each = dic[x+2]
		print(each, end = '')
	return None

encrypt(key,line)

input("\n\n...press enter to exit")


# by Stepan Paholyk 13/11/15
