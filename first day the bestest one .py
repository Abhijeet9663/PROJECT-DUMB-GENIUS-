score = 0
for i in range(3):
    print("welcome😎")


while True:
    guess = input("Who taught me this level of coding in day one? ")
    
    if guess.lower() == "chatgpt":
        print("thanks a lot to him ♥️♥️🥺")
        score = score + 1
        break
    else:
        print("try again")


while True:
    guess = input("What's my favorite colour? ")
    
    if guess.lower() == "blue":
        print("of course you knew")
        score = score + 1
        break
    else:
        print("you didn't even know this 😭")


while True:
    guess = input("Do I have a girlfriend? ")
    
    if guess.lower() == "no":
        print("yeah I guess I don't have one 😭")
        score = score + 1
        break
    else:
        print("bro why would you say yes 😭")


print("okay your final score is", score)