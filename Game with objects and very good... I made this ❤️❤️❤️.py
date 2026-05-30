
import pygame
pygame.init()
import random 
import time 
screen = pygame.display.set_mode((500,500))
time_left =30
start_time = pygame.time.get_ticks()

x= 0 
y = 500 
circle1x = 250 
circle1y= 250
circle2x= 100
circle2y= 100
circle3x=200
circle3y=200
score =0
font = pygame.font.SysFont(None , 40)

running = True 
clock = pygame.time.Clock()

while running:
	screen.fill (( 149, 69, 68)) 
	pygame.draw.circle(screen , (255,255,0), (circle1x , circle1y) , 80 )
	pygame.draw.circle(screen , (255,0,0), (circle2x , circle2y) , 80 )
	pygame.draw.circle(screen , (255,0,0), (circle3x , circle3y) , 80 )

	clock.tick(60)
	pygame.draw.rect(screen , (255,255,255) , (x, y , 50, 50 ))
	text = font.render("score =  " + str(score) , True  , (125,25, 90))
	
	screen.blit(text , (20,20))
	
	
	text3 = font.render("press only the Yellow circle😎" , True , (50 ,200 ,85) )
	
	screen.blit(text3 , (70,80))
	
	current_time= pygame.time.get_ticks()
	
	seconds_passed = (current_time - start_time) //1000
	
	time_show = time_left - seconds_passed 
	
	
	text6 = font.render("Time left = " + str(time_show) , True , (125 ,10 ,90) )
	
	screen.blit(text6 , (20,40))
	pygame.display.update()
	

	

	if x< circle1x< x+50 and y<circle1y<y+50 :
		print ("collision 🙄")
		screen.fill ((0,250,0))
		score += 1
	
		circle1x = random.randint(80 , 500)
		circle1y = random.randint(80 , 500)
		
		circle2x = random.randint(80 , 500)
		circle2y = random.randint(80 , 500)
		
		circle3x = random.randint(80 , 500)
		circle3y = random.randint(80 , 500)
		
		pygame.display.update()
		
		
	
	if x< circle2x< x+50 and y<circle2y<y+50 :
		
		screen.fill((255,0,0))
		
		text4 = font.render("you lost " , True , (0 ,0 ,0) )
		
		screen.blit(text4 , (250,250))
		pygame.display.update()
		
		time.sleep(5)
		
		running = False 
		
	
	
	if x< circle3x< x+50 and y<circle3y<y+50 :
		
		screen.fill((250,0,0))
		text4 = font.render("you lost " , True , (0 ,0 ,0) )
		
		screen.blit(text4 , (250,250))
		pygame.display.update()
	
		time.sleep(5)
		running = False 
	
	
		
	if score == 10:
		text2 = font.render("you won 😎" , True , (0 ,0 ,0) )
		
		screen.blit(text2, (250,250))
		pygame.display.update()
		
		time.sleep (5)
		running = False
		
	if time_show<0:
		text7 = font.render("time up 😎" , True , (0 ,0 ,0) )
		
		screen.blit(text7, (250,250))
		pygame.display.update()
		
		time.sleep (5)
		running = False
			
		
	
	pygame.display.update()
	
	
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			
			x , y  = event.pos
			
		if event.type == pygame.QUIT:
			running = False

pygame.quit()