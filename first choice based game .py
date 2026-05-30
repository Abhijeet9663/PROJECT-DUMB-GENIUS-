print ("welcome to a game created by Abhijit ")

print ("this is a choice based game so every choice matters choose carefully ")

guess =  input (" what is 2 +2? ")
if guess.lower() == "4":
		
	print("you move yo next level")
		
else:
	print (" you lost")
	quit()
	
guess = input(" now tell me whats the 4+8 ?")
if guess.lower() == "12":
				
	print( "you move to last level")
			
else:
	print(" you lost")	
	quit()
				
guess = input(" now tell me are you dumb?")
if guess.lower() == "yes":
	print ("you win")
else:
	print ("you lost")
	quit()

