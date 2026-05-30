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
		
