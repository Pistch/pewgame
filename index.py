import sys, pygame, time
pygame.init()

size = width, height = 800, 600
speed = [1, 1]
black = 0, 0, 0
fps = 10

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

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()