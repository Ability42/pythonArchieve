# take a break
import webbrowser, time

total_breaks = 2
break_count = 0

print("This program started on" + time.ctime())
while total_breaks > break_count:
	
	time.sleep(3)	#*60*60)
	webbrowser.open("https://www.doodle.com")
	break_count += 1

input("\n\nPlease, press the enter key to exit...")