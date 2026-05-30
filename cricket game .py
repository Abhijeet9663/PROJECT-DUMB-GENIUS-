import time 
import random
score = 0
computerscore = 0

print ("Hand cricket Game by Abhijit ")

def comp():
	print ("i choose " , Runs)
def sleep():
	time.sleep(random.uniform(1,2))


while True:
	Runs = random.randint(1,6)
	guess = int(input("choose your runs "))
	
	if guess == Runs :
		comp()
		sleep()
		print ( "Bowled 😎🤦... you are Out " )
		print ("computer thinking in his mind 🤦 --> i always knew i am mind reader i would have been succesful if my creater didn't maniputer me ")
		break 
	elif guess >6:
		print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
	else:
		comp()
		sleep()
		score += guess 
		print ("your score is ", score )
		
sleep ()		
print ("your total score is ", score)	
sleep()

print (" now I will chase your  score .... Target = ", score+1) 	


while True:
	
	Runs = random.randint(1,6)
	chase = int(input("Choose your Ball "))
	
	if chase== Runs:
		comp()
		sleep()
		print ("out wicket")
		print (" computer in his mind = oh no no no no no ..... this... can't be ... ... Am i ?? No - he just... he just got lucky   ")
		break 
	elif chase >6:
		print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
		
	else :
		comp()
		sleep ()
		computerscore += Runs 
		print (" my score is  " , computerscore )
		
		if computerscore > score :
			print ("I won ... yes  i won")
			sleep()
			print ("computer in his mind 🤦 = i always knew I am a Indian cricket team material 😎😎")
			break 
			
			
sleep()

if computerscore== score :
	print ("match draw " )
	
													
elif computerscore< score :
	print ("okay you got lucky ") 					
													
						
			
			
	
	

	