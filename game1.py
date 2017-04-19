# Daniel Zarco - dz7as

import pygame
import gamebox
camera = gamebox.Camera(1300,700)

p1_score = 0
p2_score = 0

# Replace this to from_image
plane1 = gamebox.from_color(100,100,"blue",20,40)

# Replace this to from_image
plane2 = gamebox.from_color(200,200,"red",20,40)

def tick(keys):

	camera.clear('cyan')
	global p1_score
	global p2_score

	# player 1
	if pygame.K_w in keys:
	    plane1.y -= 5
	if pygame.K_s in keys:
	    plane1.y += 5
	if pygame.K_d in keys:
	    plane1.x += 5
	if pygame.K_a in keys:
	    plane1.x -= 5

	# player 2
	if pygame.K_UP in keys:
	    plane2.y -= 5
	if pygame.K_DOWN in keys:
	    plane2.y += 5
	if pygame.K_RIGHT in keys:
	    plane2.x += 5
	if pygame.K_LEFT in keys:
	    plane2.x -= 5

	# collisions
		# collisions between planes
		# collisions between object
		# colisions between floor and plane

	# health of planes


	camera.draw(plane1)
	camera.draw(plane2)

	camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
