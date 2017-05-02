# Daniel Zarco - dz7as
# Andrew Carl - ac2mx
import pygame
import gamebox
import random

camera = gamebox.Camera(1300,700)
game = 0
count = 0
t = 0
speed = 0
rotate = 0
p1_score = 100

plane1 = gamebox.from_image(400,100,"http://i.imgur.com/Ay7WRQQ.png")
title_png = gamebox.from_image(650,125,"http://i.imgur.com/HpLlOk5.png")
top_barrier = gamebox.from_color(650,-20,"red",1300,40)
bottom_barrier = gamebox.from_color(650,720,"red",1300,40)
random_s = random.randrange(50,650)
s = gamebox.from_image(1400,random_s,"http://i.imgur.com/ULNNSrE.png")
mama = gamebox.from_image(100,350,"http://i.imgur.com/7CaRxO9.png")

stars = []
for y in range(0,1301,2):
	stars.append(gamebox.from_color(random.randrange(0,1305),y,'white',2,2))

asteroids_20 = []
for y in range(0,1100,50):
	asteroids_20.append(gamebox.from_image(random.randrange(200,1450),y,"http://i.imgur.com/UPbXoKn.png"))

asteroids_50 = []
for y in range(0,1100,50):
	asteroids_50.append(gamebox.from_image(random.randrange(200,1450),y,"http://i.imgur.com/RfeqBgU.png"))

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
	global speed
	global rotate

	if game == 0:
		if pygame.K_DOWN in keys:
			count += 1
			keys.clear()
		if pygame.K_UP in keys:
			count -= 1
			keys.clear()
		bottom0 = gamebox.from_text(camera.x, camera.y - (-180), "Use down arrow key to navigate and space to select.","Times New Roman", 30, "White")
		start_white = gamebox.from_text(camera.x, camera.y - 100, "Start", "Times New Roman", 30, "White")
		start_black = gamebox.from_text(camera.x, camera.y - 100, "Start", "Times New Roman", 30, "Black")
		start_box_white = gamebox.from_color(camera.x, camera.y - 100, 'White', 100, 50)
		how_to_play_white = gamebox.from_text(camera.x, camera.y - 50, "How To Play", "Times New Roman", 30, "White")
		how_to_play_black = gamebox.from_text(camera.x, camera.y - 50, "How To Play", "Times New Roman", 30, "Black")
		how_to_play_box_white = gamebox.from_color(camera.x, camera.y - 50, 'White', 200, 50)
		camera.clear('Black')
		camera.draw(bottom0)
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
			keys.clear()
		if pygame.K_SPACE in keys and count == 2:
			game = 2
			keys.clear()

	if game == 2:
		camera.clear('black') 
		instructions =  gamebox.from_text(camera.x, camera.y - 220, "INSTRUCTIONS","Times New Roman", 40, "White")
		l1 = gamebox.from_text(camera.x, camera.y - 150, "1. The objective of the game is to fly the furthest away from Planet Sully.","Times New Roman", 30, "White")
		l2 = gamebox.from_text(camera.x, camera.y - 120, "2. To navigate the ship, you use the arrow keys and have to constantly move forward.","Times New Roman", 30, "White")
		l3 = gamebox.from_text(camera.x, camera.y - 90, "3. The further you get, the higher your score.","Times New Roman", 30, "White")
		l4 = gamebox.from_text(camera.x, camera.y - 60, "4. If your ship touches the asteroids, your ship takes damage.","Times New Roman", 30, "White")
		l5 = gamebox.from_text(camera.x, camera.y - 30, "5. Your only saviors are the Sully-droids which will will bring your slush fund back to 100%.","Times New Roman", 30, "White")
		l6 = gamebox.from_text(camera.x, camera.y - 0, "6. You die and the game ends when the slush fund gets to 0.","Times New Roman", 30, "White")
		bottom = gamebox.from_text(camera.x, camera.y - (-90), "Press space to play.","Times New Roman", 30, "White")
		camera.draw(instructions)
		camera.draw(l1)
		camera.draw(l2)
		camera.draw(l3)
		camera.draw(l4)
		camera.draw(l5)
		camera.draw(l6)
		camera.draw(bottom)
		if pygame.K_SPACE in keys:
			game = 1
	if game == 1:
		player_controls(keys)
		camera.clear('black')

		plane1.x -= 3

		# boost - Easter egg cheat (When your dad donates a million dollars to UVA and T Sully accepts)
		if pygame.K_b in keys:
			plane1.x += 100	

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
				p1_score += -1

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

		if plane1.touches(top_barrier):
			plane1.move_to_stop_overlapping(top_barrier)
		if plane1.touches(bottom_barrier):
			plane1.move_to_stop_overlapping(bottom_barrier)

		s.rotate(10+rotate)
		s.x -= 2 + speed
		if s.left < -10:
			s.x = 1500
			s.y = random.randrange(50,650)

		if plane1.touches(s):
			s.x = 1500
			s.y = random.randrange(50,650)
			p1_score = 100
			speed += 1
			rotate += 0.5

		mama.x -= 1
		if mama.right < 0:
			mama.x = -200
			mama.y = 1800

		camera.draw(mama)

		for asteroid in asteroids_20:
			camera.draw(asteroid)
		for asteroid in asteroids_50:
			camera.draw(asteroid)
		for star in stars:
			camera.draw(star)

		if p1_score <= 0:
			p1_score = 0
		camera.draw(gamebox.from_text(200, 30, str("Slush Fund - ")+str(p1_score)+str("%"), "Arial", 30, "white", True))
		camera.draw(plane1)
		camera.draw(s)
		camera.draw(top_barrier)
		camera.draw(bottom_barrier)
		camera.draw(gamebox.from_text(1150, 30, str("Score: ")+str(t), "Arial", 30, "white", True))
		if p1_score <= 0:
			camera.draw(gamebox.from_text(650, 100, str("Looks like you need to raise tuition again!"), "Arial", 40, "red", True))
			gamebox.pause()
		t += 1	

	camera.display()
ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)