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
							
	