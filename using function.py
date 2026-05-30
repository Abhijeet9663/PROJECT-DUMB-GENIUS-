
def ask(q , a , attempts ):
	while attempts > 0:
		guess = input(q + "" )
		if guess.lower().strip() == a.lower().strip():
			print ("correct 😁 😁 genius")
			return True
		else:
			print ("wrong bitch!!  ( sorry kabhi kabhi muh se nikal jata hai 🤣) ") 
			attempts -= 1
	print (" you failed i guess I am not sorry you really are dumb 🤣🤣💀") 
	return False	
	quit()		

score = 0

if ask ( " what is the my name " , "abhijit " , 2):
	score += 1 
else: 
	score -= 0.1

if ask ( " what is the my favourite game " , "free fire " , 2 ):
	score += 1 
else:
	score -= 0.1					

if ask ( " what is the name of my country " , "india " , 3 ):
	score += 1
else:
	score -= 0.1	

print ("your final score is " , score)
