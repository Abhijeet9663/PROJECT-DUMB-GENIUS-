
import pygame
pygame.init()
import random 
import time 
screen = pygame.display.set_mode((500,500))

x= 0 
y = 500 
circlex = 250 
circley= 250
score =0
font = pygame.font.SysFont(None , 40)

running = True 
clock = pygame.time.Clock()

while running:
	keys = pygame.key.get_pressed()
	screen.fill (( 149, 69, 68)) 
	pygame.draw.circle(screen , (255,255,0), (circlex , circley) , 80 )

	clock.tick(60)
	pygame.draw.rect(screen , (255,255,255) , (x, y , 50, 50 ))
	text = font.render("score =  " + str(score) , True  , (125,125, 50))
	
	screen.blit(text , (20,20))

	if x< circlex< x+50 and y<circley<y+50 :
		print ("collision 🙄")
		screen.fill ((255,0,0))
		score += 1
	
		circlex = random.randint(80 , 500)
		circley = random.randint(80 , 500)
		
		pygame.display.update()
		
	if score == 10:
		text2 = font.render("you won 😎" , True , (0 ,0 ,0) )
		
		screen.blit(text2, (250,250))
		pygame.display.update()
		
		time .sleep (5)
		quit()
	
	pygame.display.update()
	
	
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			
			x , y  = event.pos
			
		
		if event.type == pygame.QUIT:
			running = False 

			
pygame.quit() 