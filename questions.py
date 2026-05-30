score = 0
print ("Hello world")

questions = ["who is the president of india" , "who is Ms dhoni" , "whats the name of the best midern day odi cricketer "]

answers = ["modi", "cricketer" , "virat"]


for i in range(3):
	while True:
		guess = input(questions[i] + "")
		
		if guess.lower()== answers[i]:
			print ("correct genius" )
			score += 1
			break
			
		else:
			print ("this is what we expect from you ")
			score -= 0.1
					

print("okay your final score is" , score )				
		