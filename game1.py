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
	global p1_score
	global p2_score
	player_controls(keys)
	camera.clear('black')

	plane1.x -= 3
	plane2.x -= 3

	# beam
	if pygame.K_SPACE in keys:
		plane2.x += 100

	for star in stars:
		star.x -= 2
		if star.left < 0:
			star.x = 1300
			star.y = random.randrange(0,1305)
			star.size = 2,2

	for asteroid in asteroids_20:
		asteroid.x -= 10
		asteroid.rotate(10)
		if asteroid.left < -100:
			asteroid.x = 1350
			asteroid.y = random.randrange(0,705)

	for asteroid in asteroids_20:
		if plane1.touches(asteroid):
			plane1.move_to_stop_overlapping(asteroid)
			p1_score -= 1
		if plane2.touches(asteroid):
			plane2.move_to_stop_overlapping(asteroid)
			p2_score -= 1

	for asteroid in asteroids_50:
		asteroid.x -= 10
		asteroid.rotate(10)
		if asteroid.left < -100:
			asteroid.x = 1350
			asteroid.y = random.randrange(0,705)

	for asteroid in asteroids_50:
		if plane1.touches(asteroid):
			plane1.move_to_stop_overlapping(asteroid)
			p1_score -= 1
		if plane2.touches(asteroid):
			plane2.move_to_stop_overlapping(asteroid)
			p2_score -= 1

	if p1_score <= 0:
		camera.draw(gamebox.from_text(650, 100, str("Player 2 wins!"), "Arial", 40, "red", True))
		gamebox.pause()

	elif p2_score <= 0:
		camera.draw(gamebox.from_text(650, 100, str("Player 1 wins!"), "Arial", 40, "red", True))
		gamebox.pause()

	for asteroid in asteroids_20:
		camera.draw(asteroid)
	for asteroid in asteroids_50:
		camera.draw(asteroid)
	for star in stars:
		camera.draw(star)

	camera.draw(gamebox.from_text(100, 30, str("Player 1 - "), "Arial", 20, "white", True))
	camera.draw(gamebox.from_text(200, 30, str(p1_score), "Arial", 40, "white", True))
	camera.draw(gamebox.from_text(1110, 30, str("Player 2 - "), "Arial", 20, "white", True))
	camera.draw(gamebox.from_text(1210, 30, str(p2_score), "Arial", 40, "white", True))

	camera.draw(plane1)
	camera.draw(plane2)

	camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)