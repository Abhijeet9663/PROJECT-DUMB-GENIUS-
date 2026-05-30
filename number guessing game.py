high= 100
low = 1
import random 
import time 

print (" hello let's play a game pick a number between 1 and 100.. ")

time.sleep(random.uniform(1,3))

print("okay let's start the game ")

time.sleep(random.uniform(1,3))


while True:
	guess = ( low + high )//2
	
	time.sleep(random.uniform(1,3))
	print ("I guess the number " , guess )
	
	
		
	time.sleep(random.uniform(1,3))
	feedback = input(" is it H = tooo high  ,L = too low C= correct ").lower().strip()
	
	if feedback == "h":
		high = guess - 1 
		
	elif feedback== "l":
		low = guess + 1 
		
	elif feedback== "c" :
		print ("yay I won 😎😎")
		break
	
		
	else:
		print ("give a real feedback🤦😁") 
			
	if low > high :
		print (" umm... are you cheating ?.. i guess you are inspired by your EX??.😂")	
		
		
