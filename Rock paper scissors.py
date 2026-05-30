print ("let's play rock paper and scissors of three attempts  ")
import random 
import time 
userscore = 0
computerscore = 0
attempts = 0 

choice = ["rock", "paper" , "scissors"]


while attempts < 3 :
	computer = random.choice(choice)
	msg= input ("choose one rock, paper, scissors ").lower().strip()
	print ("you chose " , msg)

	time.sleep(random.uniform(1,3))

	if msg == computer:
		print("i chose" , computer)
		attempts += 1
	
		time.sleep(random.uniform(1,3))
		print ("draw..")
	
	elif msg == "rock" and computer == "paper":
		print("i chose" , computer)
		attempts += 1
	
		time.sleep(random.uniform(1,3))
		print ("you lost paper beats rock")
		computerscore += 1
	
	elif msg == "rock" and computer== "scissors":
		print("i chose" , computer)
		attempts += 1
		
		time.sleep(random.uniform(1,3))
		print (" you won rock beats scissors")
		userscore += 1 
	

	elif msg == "paper" and computer== "scissors":
		print("i chose" , computer)
		attempts += 1
		
		time.sleep(random.uniform(1,3))
		print ("you lost scissors beats paper")	
		computerscore += 1
	
	
	elif msg == "paper" and computer== "rock":
		print("i chose" , computer)
		attempts += 1

		time.sleep(random.uniform(1,3))
		print ("you won paper beats rock ")
		userscore += 1 


	elif msg == "scissors" and computer== "rock":
		print("i chose" , computer)
		attempts += 1
	
		time.sleep(random.uniform(1,3))
		print ("you lost rock beats scissors")
		computerscore += 1			
			
									

	elif msg == "scissors" and computer== "paper":
		print("i chose" , computer)
		attempts += 1
	
		time.sleep(random.uniform(1,3))
		print ("you won scissors beats paper")
		userscore += 1 		
	
	else:
		print ("pick one of these..... ")	
		
		
		
if userscore == computerscore :
	print ("computer score = " , computerscore ,  "your score = " , userscore )
	time.sleep(random.uniform(1,3))
	
	print ("game tied")
	
elif userscore > computerscore :
	print ("computer score = " , computerscore  , "your score = " , userscore )
	time.sleep(random.uniform(1,3))
	print ("you won 🎖️🏆" )
	

elif userscore < computerscore :
	print ("computer score = " , computerscore , "your score = "  ,  userscore )
	time.sleep(random.uniform(1,3))
	
	print ("you lost 😵")
	
	
			

	
	
	
