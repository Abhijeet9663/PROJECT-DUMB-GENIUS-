def playRPS() :
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
		


def numberguess() :
	import random  
  
	print("random number gussi game only 3 attempts")  
	  
	attempts = 3  
	  
	number = random.randint(1,10)
	  
	while True:  
		guess= int(input ("guess your number: " ))   
		if guess == number:  
			print ("you won ")  
			  
			ask = input ("do you want to play again yes / no ").lower().strip()  
			if ask== "yes":  
				print ("okay let's restart ")  
				attempts = 3
				number = random.randint(1,10)
		
			
		
			else:  
				break   
		  
		elif guess<number:  
			print ("too low")  
			attempts -= 1  
			print ("attempts left: ", attempts)  
			  
		else:  
			print("too high")  
			attempts -= 1  
			print ("attempts left: ", attempts)  
			  
		if attempts == int(0):  
			print ("you lost ")  
			  
			ask = input ("do you want to play again yes / no ").lower().strip()  
			if ask== "yes":  
				print ("okay let's restart ")  
				attempts = 3  
				number = random.randint(1,10)
			else:  
				break	  
		  
	  
	  
	
def chatbot() :
	print (" chatbot created by Abhijit  ")
	import random
	import time 
	name = ""
	while True:
		
		msg = input("you: ").lower().strip()
		
		
		if "sad"in msg or "depressed" in msg or "cry" in msg or "bad" in msg or "worst day" in msg:
			replies = [ " oh I am sorry bro ❤️, everything will be okay" , " stay strong bro ❤️" , "bro stay helath and remember this too will pass" ]
			time.sleep(2)
			print ("bot:" , random.choice(replies) )
					
		elif "happy"in msg or "great" in msg or "best day" in msg:
			time.sleep(random.uniform(1,3))
			replies = ["wonderful that's great enjoy" , "enjoy your day bro " , "you are doing great"  ]
			
			print ("bot:" , random.choice(replies) )
	
		elif "hello" in msg or "hey" in msg or "hii" in msg :
			
			replies = ["hey bro 👋", "hello I am a learning bot" , "hey there" , "hello 👋🤗"]
			time.sleep(1)
			print (" bot :" , random.choice(replies))
			
		elif msg in ("how are you", "how r u") :
			time.sleep(random.uniform(1,3))
			print (" bot : thanks i am fine ♥️") 
			
		elif msg in ["bye" , "byy" , "by" , "tata" ]:
			time.sleep(random.randint(1,3))
			print ("bot : good bye thanks nice to talk to you  👍", name )
			break
		elif "my name is"  in msg:
			time.sleep(2)
			name = msg.replace ( "my name is ",  "" ).strip() 
		
			print ("bot : thanks for telling your name")	
			
		elif msg  in ("what is my name" , "what's my name " , "whats my name" ):
			time.sleep( random.uniform(1,3))
			if name == "":
				print ("you have not told me you name bro maybe if i were a magician i would have been better so that I coud have guessed your name ... i guess i came in wrong lane 😂😂 you know i always wanted to become a magician but my creator is bit of you know manipulative you know 👉👈👉👈 😂🤦‍♀️ ( okay somtim i come to rant mode 🥺🙄🙄) ")
			else:
				print (" bot : your name is " , name )
		
					
			
		elif "jokes" in msg  or "laugh" in msg or "funny" in msg or"roast" in msg:
			time.sleep(random.uniform(1,3))
			replies = ["jokes ? isn't your life a joke 🤣 (okay sorry🤦‍♀️) " , " Do you know i am about to steal the jobs of  ChatGPT  Gemini , Grok 🏋️👉👈(okay in dreams only 🤣 of course)" , "Do you know what's the similarity between me(chatbot) and you ... we both don't have a girlfriend 🤣🤣"]
			print ("bot :", random.choice(replies))
		else:
			time.sleep( random.uniform(1,3 ))
			print ("bot : I am not that intelligent yet my creator is kinda dumb still although he has added more these great things now .. but still very limited 😂😂😂😅  .... i guess i should not roast my creator tha much he will cry in dreams 😂😂")	
	
										
def computerguess():
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
			
																													
def calculator():
	print (" calculater by abhiit....  yeah little bit of show off  of course🤣😎😎 ")

	while True:
		while True:
			try:
				n1 = int(input("enter your first number: "))
				break 
			except:
				print (" enter a valid number ")	
		while True:
			try:
				n2 = int(input( "enter your second number : "))
				break
			except:
				print("enter a valid number")
	
		op = input("choose the operation + ,  - , * , / ")
	
		if op == "+":
			print ("your final answer is: " , n1 + n2 )
	
		elif op == "-":
			print (" your final answer is :"  , n1- n2)
		
		elif op == "*":
			print ( " your final answer is: " , n1 * n2 )
		
		elif op == "/":
			if n2 ==  0:
				print ("invalid operations can't be decidd by zero ")
				
			else:
				print ( "your final answer is :" , n1 / n2 ) 
		
		else:
			print (" bakchodi mat kar laude 💀💀👺... aakh nhi hai kya choose kar na Shanti se  ") 				
		ask = input(" do you want to continue the calculator yes/ no " ) 	
		if ask.lower().strip() == "no":
			break
			
																							
while True:
	print("welcome to games By Abhijit")

	new= input ("which game you want to play 1 = number guessing game ,  2= computer guess your number  3 = Rock paper and scissors  4 = chat with a chatbot  5 = calculator  --->   choose 1/2/3/4/ 5 ").lower().strip()
	
	if new == "1":
		numberguess()
	
	elif new == "2":
		computerguess ()
		
	elif new == "3":
		playRPS()
		
	elif new == "4":
		chatbot()
		
	elif new == "5":
		calculator ()
		
	else:
		print (" choose a correct game to play 🥺")
		
	lobby = input(" do you want to return to lobby --> yes/ No " )
	if lobby == "yes":
		print ("welcome back")
		
	elif lobby == "no":
		break 
	else :
		print ("choose carefully" )
																																																																																																																																																																																							