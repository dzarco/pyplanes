# Daniel Zarco - dz7as
# Andrew Carl - ac2mx

# Things we should do
#	Make sprite images for when a rocket crashes into an asteroid and when the plane has lower tiers of health
#	Make different sized objects
#	Make recoverable health
#	Make powerups and mario-kart style add-ons
#	Menu to start game and explain how to play?
# 	If the rocket disappears from the screen, then have it re-spawn with a certain amount of health subracketed
#	Draw planets and other things in the background

import pygame
import gamebox
import random

camera = gamebox.Camera(1300,700)
game = 0
count = 0
p1_score = 100
p2_score = 100

plane1 = gamebox.from_image(400,100,"Small_Space_Ship.png")
plane2 = gamebox.from_image(400,600,"Small_Space_Ship.png")

stars = []
for y in range(0,1301,2):
	stars.append(gamebox.from_color(random.randrange(0,1305),y,'white',2,2))

asteroids_20 = []
for y in range(0,1100,50):
	asteroids_20.append(gamebox.from_image(random.randrange(200,1300),y,"20_Space_Rock.png"))

asteroids_50 = []
for y in range(0,1100,50):
	asteroids_50.append(gamebox.from_image(random.randrange(200,1300),y,"50_Space_Rock.png"))

def player_controls(keys):
	if pygame.K_w in keys:
	    plane1.y -= 5
	if pygame.K_s in keys:
	    plane1.y += 5
	if pygame.K_d in keys:
	    plane1.x += 5
	if pygame.K_a in keys:
	    plane1.x -= 5
	if pygame.K_UP in keys:
	    plane2.y -= 5
	if pygame.K_DOWN in keys:
	    plane2.y += 5
	if pygame.K_RIGHT in keys:
	    plane2.x += 5
	if pygame.K_LEFT in keys:
	    plane2.x -= 5

def tick(keys):
	global game
	global count
	if game == 0:
		if pygame.K_DOWN in keys:
			count += 1
			keys.clear()
		title = gamebox.from_text(camera.x, camera.y - 250, "THIS IS A SHIT GAME", "Times New Roman", 50, "White", bold=True)
		subtitle = gamebox.from_text(camera.x, camera.y - 200, "By Danial and Andrew", "Times New Roman", 20, "White")
		start_white = gamebox.from_text(camera.x, camera.y - 100, "Start", "Times New Roman", 30, "White")
		start_black = gamebox.from_text(camera.x, camera.y - 100, "Start", "Times New Roman", 30, "Black")
		start_box_white = gamebox.from_color(camera.x, camera.y - 100, 'White', 100, 50)
		how_to_play_white = gamebox.from_text(camera.x, camera.y - 50, "How To Play", "Times New Roman", 30, "White")
		how_to_play_black = gamebox.from_text(camera.x, camera.y - 50, "How To Play", "Times New Roman", 30, "Black")
		how_to_play_box_white = gamebox.from_color(camera.x, camera.y - 50, 'White', 200, 50)
		camera.clear('Black')
		camera.draw(start_white)
		camera.draw(how_to_play_white)
		if count == 1:
			camera.draw(start_box_white)
			camera.draw(start_black)
			print(count)
		if count == 2:
			camera.draw(how_to_play_box_white)
			camera.draw(how_to_play_black)
			print(count)
		if count == 3:
			count = 0
		camera.draw(title)
		camera.draw(subtitle)
		camera.display()
		if pygame.K_SPACE in keys and count == 1:
			game = 1