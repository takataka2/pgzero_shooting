import pgzrun
import math

WIDTH = 800
HEIGHT = 600

player = Actor('playership1_blue',(600,100))
enemy = Actor('enemyred1',(200,500))

angle = enemy.angle_to(player)
distance = enemy.distance_to(player)

rad = math.radians(-angle)
targetx = enemy.x + math.sin(rad) * distance
targety = enemy.y + math.cos(rad) * distance


def draw():
    screen.clear()
    player.draw()
    enemy.draw()
    screen.draw.line((enemy.x,enemy.y),(player.x,player.y),'RED')
    screen.draw.text('Angle:' + str(angle),(50,50))
    screen.draw.text('Distance:' + str(distance),(50,100))

pgzrun.go()