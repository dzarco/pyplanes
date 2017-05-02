# Daniel Zarco - dz7as
# Andrew Carl - ac2mx

# Things we should do
#	Menu to start game and explain how to play?
# 	If the rocket disappears from the screen, then have it re-spawn with a certain amount of health subracketed
#	Draw planets and other things in the background

# Add in pause
# add in immunity or a shield when respawning
# stop subracting points for s things
# control frequency of s

# Instructions
# Display score
# Button to play again
# Make sure life = 0
# Move time to top right

# Increasing difficulty

import pygame
import gamebox
import random

camera = gamebox.Camera(1300,700)
game = 0
count = 0
t = 0
p1_score = 100

plane1 = gamebox.from_image(400,100,"Small_Space_Ship_35.png")

title_png = gamebox.from_image(650,125,"Title_small.png")

top_barrier = gamebox.from_color(650,-20,"red",1300,40)
bottom_barrier = gamebox.from_color(650,720,"red",1300,40)

random_s = random.randrange(50,650)
s = gamebox.from_image(1400,random_s,"Mother_of_God_No.png")
mama = gamebox.from_image(100,350,"PLANET_SULLY.png")

stars = []
for y in range(0,1301,2):
	stars.append(gamebox.from_color(random.randrange(0,1305),y,'white',2,2))

asteroids_20 = []
for y in range(0,1100,50):
	asteroids_20.append(gamebox.from_image(random.randrange(200,1450),y,"20_Space_Rock.png"))

asteroids_50 = []
for y in range(0,1100,50):
	asteroids_50.append(gamebox.from_image(random.randrange(200,1450),y,"50_Space_Rock.png"))

def player_controls(keys):
	if pygame.K_UP in keys:
	    plane1.y -= 5
	if pygame.K_DOWN in keys:
	    plane1.y += 5
	if pygame.K_RIGHT in keys:
	    plane1.x += 5
	if pygame.K_LEFT in keys:
	    plane1.x -= 5

def tick(keys):
	global game
	global count
	global p1_score
	global t
	if game == 0:
		if pygame.K_DOWN in keys:
			count += 1
			keys.clear()
		if pygame.K_UP in keys:
			count -= 1
			keys.clear()
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
		if count == 2:
			camera.draw(how_to_play_box_white)
			camera.draw(how_to_play_black)
		if count == 3:
			count = 0
		if count == -1:
			count = 2
		camera.draw(title_png)
		camera.display()
		if pygame.K_SPACE in keys and count == 1:
			game = 1
	if game == 1:
		player_controls(keys)
		camera.clear('black')

		plane1.x -= 3

		# beam - Easter egg cheat (When you dad donates a million dollars to UVA and T Sully accepts)
		if pygame.K_b in keys:
			plane1.x += 100	

		# plane coming out of frame
		if plane1.left < -50: 
			plane1.x = 650
			plane1.y = random.randrange(100,600)
			p1_score -= 10	

		for star in stars:
			star.x -= 2
			if star.left < 0:
				star.x = 1300
				star.y = random.randrange(0,1305)
				star.size = 2,2
		a_20 = 0
		for asteroid in asteroids_20:
			asteroid.x -= 10
			if a_20 % 2 == 0:
				asteroid.rotate(10)
			else:
				asteroid.rotate(-10)
			if asteroid.left < -100:
				asteroid.x = 1350
				asteroid.y = random.randrange(0,705)
			a_20 += 1

		for asteroid in asteroids_20:
			if plane1.touches(asteroid):
				plane1.move_to_stop_overlapping(asteroid)
				p1_score -= 1

		a_50 = 0
		for asteroid in asteroids_50:
			asteroid.x -= 10
			if a_50 % 2 == 0:
				asteroid.rotate(10)
			else:
				asteroid.rotate(-10)
			if asteroid.left < -100:
				asteroid.x = 1350
				asteroid.y = random.randrange(0,705)
			a_50 += 1

		for asteroid in asteroids_50:
			if plane1.touches(asteroid):
				plane1.move_to_stop_overlapping(asteroid)
				p1_score -= 1

		if plane1.touches(s):
			s.x = 1500
			s.y = random.randrange(50,650)
			p1_score = 100

		if plane1.touches(top_barrier):
			plane1.move_to_stop_overlapping(top_barrier)
		if plane1.touches(bottom_barrier):
			plane1.move_to_stop_overlapping(bottom_barrier)

		s.rotate(-10)
		s.x -= 2
		if s.left < -10:
			s.x = 1500
			s.y = random.randrange(50,650)

		mama.x -= 1
		if mama.right < 0:
			mama.x = -200
			mama.y = 1800

		camera.draw(mama)
		camera.draw(gamebox.from_text(650, 30, str(t), "Arial", 20, "white", True))

		for asteroid in asteroids_20:
			camera.draw(asteroid)
		for asteroid in asteroids_50:
			camera.draw(asteroid)
		for star in stars:
			camera.draw(star)

		camera.draw(gamebox.from_text(200, 30, str("Slush Fund - ")+str(p1_score)+str("%"), "Arial", 30, "white", True))
		#camera.draw(gamebox.from_text(450, 30, str(p1_score)+str("%"), "Arial", 20, "white", True))
		if p1_score <= 0:
			p1_score = 0
		#else:
		#	camera.draw(gamebox.from_text(350, 30, str(p1_score), "Arial", 20, "white", True))

		camera.draw(plane1)
		camera.draw(s)
		camera.draw(top_barrier)
		camera.draw(bottom_barrier)

		if p1_score <= 0:
			p1_score = 0
			camera.draw(gamebox.from_text(650, 100, str("Looks like you need to raise tuition again!"), "Arial", 40, "red", True))
			gamebox.pause()
			game = 0
		t += 1	

	camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)