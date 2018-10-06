import sys, pygame, time

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
fps = 200


def get_speed():
    keys_pressed = pygame.key.get_pressed()
    speed = [0, 0]
    if keys_pressed[pygame.K_d]:
        if ballrect.right > width:
            speed[0] = 0
        else:
            speed[0] = speed[0] + 1

    if keys_pressed[pygame.K_a]:
        if ballrect.left < 0:
            speed[0] = 0
        else:
            speed[0] = speed[0] - 1

    if keys_pressed[pygame.K_s]:
        if ballrect.bottom > height:
            speed[0] = 0
        else:
            speed[1] = speed[1] + 1

    if keys_pressed[pygame.K_w]:
        if ballrect.top < 0:
            speed[1] = 0
        else:
            speed[1] = speed[1] - 1

    return speed

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


    ballrect = ballrect.move(get_speed())

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
