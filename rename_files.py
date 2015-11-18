# rename a files in directory by using os module
# if a file name contains a digits - they will be delete

import os,re

def rename_files():
#	(1) get files names from folders
	file_list = os.listdir(path="D:/_programming/UdaCity/prank/")
	print(file_list)
	saved_path = os.getcwd()
	print('Current working directory is ' + saved_path)
	os.chdir(path="D:/_programming/UdaCity/prank/")
#	(2) for each file, rename filename
	for file_name in file_list:
		new_file_name = re.sub('[0123456789]','',file_name) # cool things
		os.rename(file_name, new_file_name)
	os.chdir(saved_path)

rename_files()
input("\n\n...press any key...")
