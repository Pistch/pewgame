import sys, pygame, time

from modules.Physics import Physics

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
fps = 200

physics = Physics(size)
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
cur_time = time.time() * 1000

while 1:
    inner_cur_time = time.time() * 1000
    if (cur_time > inner_cur_time - (1000 / fps)):
        continue

    cur_time = inner_cur_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(physics.get_speed(ballrect.left, ballrect.top))

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
