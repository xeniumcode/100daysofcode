import platform
import sys
import datetime
import requests

arr = sys.argv

if "-help" in arr :
	print("""Written by Aman 

Flag
	
	-help  		: Print this help output
	-time  		: Return current time 
	-system	 	: Print operating system info 
	
Argument

	ip 		: Return the public ipaddress of system
	status		: Return internet status
	temp		: Print temprature  of System""")

elif "-time" in arr :
	time = str(datetime.datetime.now())[11:19]
	print("Time :",time)

elif "-system" in arr :
	print(platform.system())

elif "ip" in arr :
	user_agent = {'User-agent': 'curl'}	
	print(requests.get("https://ipaddr.in/", headers = user_agent).text , end="")
" Timeup during coding , but can do after some searching . "
