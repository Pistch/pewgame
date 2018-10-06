import pygame

class Physics:
    speed = [0, 0]
    dimensions = [800, 600]
    acceleration_rate = 1
    slow_rate = 0.1

    def __init__(
            self,
            field_dimensions,
            player_dimensions = [111, 111],
            slow_rate = 0.3,
            acceleration_rate = 1,
            max_speed = 15
    ):
        print('Physics module initiated')
        self.dimensions = list(field_dimensions)
        self.player_dimensions = player_dimensions
        self.slow_rate = slow_rate
        self.acceleration_rate = acceleration_rate
        self.max_speed = max_speed

    def get_speed(self, top = 0, left = 0):
        keys_pressed = pygame.key.get_pressed()

        speed = [0,0]

        if keys_pressed[pygame.K_w]:
            speed[1] = speed[1] - self.acceleration_rate

        if keys_pressed[pygame.K_s]:
            speed[1] = speed[1] + self.acceleration_rate

        if keys_pressed[pygame.K_a]:
            speed[0] = speed[0] - self.acceleration_rate

        if keys_pressed[pygame.K_d]:
            speed[0] = speed[0] + self.acceleration_rate

        speed = self.resolve_collision(speed, [top, left])
        self.update_speed(speed)

        return self.speed

    def update_speed(self, shift):
        self.speed[0] = self.resolve_delta(self.speed[0], shift[0])
        self.speed[1] = self.resolve_delta(self.speed[1], shift[1])

    def resolve_delta(self, was, delta):
        if (was == 0 and delta == 0): return 0

        if (delta != 0):
            if (was + delta > self.max_speed): return self.max_speed
            if (was + delta < -self.max_speed): return -self.max_speed
            return was + delta

        if (was < 0):
            return was + self.slow_rate
        else:
           return was - self.slow_rate

    def resolve_collision(self, speed, pos):
        speed[0] = self.stop_if_collide(speed[0], self.dimensions[0], pos[0], self.player_dimensions[0])
        speed[1] = self.stop_if_collide(speed[1], self.dimensions[1], pos[1], self.player_dimensions[1])
        return speed

    def stop_if_collide(self, speed, max, pos, player_size):
        if (pos + speed > max - player_size):
            print('collision with max value')
            return max - player_size - pos
        if (pos + speed < 0):
            print('collision with min value')
            return -pos
        return speed