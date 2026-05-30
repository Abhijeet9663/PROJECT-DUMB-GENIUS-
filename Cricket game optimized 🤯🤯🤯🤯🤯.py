import time 
import random
score = 0
computerscore = 0

print ("Hand cricket Game by Abhijit ")

def userbattingfirst():
	global score 
	global computerscore
	while True:
		Runs=random.randint(1,6)
		guess = int(input("choose your runs "))
		
		if guess == Runs:
			comp(Runs)
			sleep()
			print ( "Bowled 😎🤦... you are Out " )
			print ("computer thinking in his mind 🤦 --> i always knew i am mind reader i would have been succesful if my creater didn't maniputer me ")
			break 
		elif guess >6:
			print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
		else:
			comp(Runs)
			sleep()
			score += guess 
			print ("your score is ", score )
			
	sleep ()		
	print ("your total score is ", score) 



def computerbattingsecond() :
	global score 
	global computerscore 
	while True:
		
		Runs = random.randint(1,6)
		chase = int(input("Choose your Ball "))
		
		if chase== Runs:
			comp(Runs)
			sleep()
			print ("out wicket")
			print (" computer in his mind = oh no no no no no ..... this... can't be ... ... Am i ?? No - he just... he just got lucky   ")
			break 
		elif chase >6:
			print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
			
		else :
			comp(Runs)
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
		
		
		
def computerbattingfirst():
	global score 
	global computerscore 
		
	while True:
		
		Runs = random.randint(1,6)
		chase = int(input("Choose your Ball "))
		
		if chase== Runs:
			comp(Runs)
			sleep()
			print ("out wicket")
			print (" computer in his mind = oh no no no no no ..... this... can't be ... ... Am i ?? No - he just... he just got lucky   ")
			break 
		elif chase >6:
			print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
			
		else :
			comp(Runs)
			sleep ()
			computerscore += Runs 
			print (" my score is  " , computerscore )
			
			
	sleep ()		
	print (" My total score is ", computerscore )	
	sleep()
	
	print (" now you will chase your  score .... Target = ", computerscore+1) 
	
def userbattingsecond():
	global score 
	global computerscore 
				
	while True:
		Runs = random.randint(1,6)
		guess = int(input("choose your runs "))
		
		if guess == Runs :
			comp(Runs)
			sleep()
			print ( "Bowled 😎🤦... you are Out " )
			print ("computer thinking in his mind 🤦 --> i always knew i am mind reader i would have been succesful if my creater didn't manipute me ")
			break 
		elif guess >6:
			print ("choose between 1 to 6 have you ever played cricket dumbo 😂")
		else:
			comp(Runs)
			sleep()
			score += guess 
			print ("your score is ", score )
			
			if score > computerscore :
				print ("you won😤👺")
				sleep()
				print ("computer in his mind --> calm down bro he just .... got... lucky ")
	
		
	
		sleep()
	
	if computerscore== score :
		print ("match draw " )
		
														
	elif computerscore > score :
		print ("I areday knew I was going to win this from the first ball we played actually I would have been a replacement of Virat if my creator abhijit would have let me play 🥺🥺👉👈") 					
					
		
								
def comp(Runs):
	print ("i choose " , Runs)
def sleep():
	time.sleep(random.uniform(1,2))													
					

while True:
	Toss = ["heads" , "tails"]
	
	result = random.choice(Toss)
	select = input(" what's  do you choose heads / tails ").lower().strip()
	
	if select == result :
		print ("you won the toss !! ")
		des = input("what do your choose bat / bowl ").lower().strip()
		
		if des == "bat":
			print ("you choose to bat")
			userbattingfirst()
			
			print ("okay I will chase now target =  ", score + 1)
			computerbattingsecond()
			
		elif des == "bowl":
			print ("okay you choose to bowl")
			
			computerbattingfirst()
			
			userbattingsecond()
		
		else:
			print ("choose a valid option")
			
		
	else:
		print ("you lost the toss")
		print ("I will bat first 😎😎")
		
		computerbattingfirst()
		userbattingsecond ()
		
	
	lobby = input ("do you want to play again? yes/no ").lower().strip()
	
	if lobby == "yes":
		print ("okay let's play again ")
	
	elif lobby == "no":
		print ("okay goodbye" ) 
		break 	