import pygame

class Physics:
    speed = [0, 0]

    def __init__(
            self,
            field_dimensions,
            player_dimensions = [111, 111],
            gravity = 0.92,
            slow_rate = 0.95,
            acceleration_rate = 0.7,
            max_speed = 15
    ):
        print('Physics module initiated')
        self.dimensions = list(field_dimensions)
        self.player_dimensions = player_dimensions
        self.slow_rate = slow_rate
        self.gravity = gravity
        self.acceleration_rate = acceleration_rate
        self.max_speed = max_speed

    def get_speed(self, left = 0, top = 0):
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

        speed = self.resolve_collision(speed, [left, top])
        self.update_speed(speed, top > self.dimensions[1] - self.player_dimensions[1] - 1)

        return self.speed

    def update_speed(self, shift, close_to_bottom = False):
        self.speed[0] = self.resolve_delta(self.speed[0], shift[0], 0, close_to_bottom)
        self.speed[1] = self.resolve_delta(self.speed[1], shift[1], 1, close_to_bottom)

    def resolve_delta(self, was, delta, current_coord, close_to_bottom = False):
        if (was == 0 and delta == 0 and current_coord == 0): return 0

        if (delta != 0):
            if (was + delta > self.max_speed): return self.max_speed
            if (was + delta < -self.max_speed): return -self.max_speed
            return was + delta

        if current_coord == 0:
            if delta == 0 and (was < 0.03 and was > -0.03): return 0
            return was * self.slow_rate
        else:
            if was > -1 and was <= 0: return 0.6
            if close_to_bottom and was > -1.3 and was <= 0: return 0

            if was < 0:
                return was * self.gravity
            else:
                return was / self.gravity

    def resolve_collision(self, speed, pos):
        speed[0] = self.stop_if_collide(speed[0], self.dimensions[0], pos[0], self.player_dimensions[0], 0)
        speed[1] = self.stop_if_collide(speed[1], self.dimensions[1], pos[1], self.player_dimensions[1], 1)
        return speed

    def stop_if_collide(self, speed, max, pos, player_size, current_coord):
        if (pos + speed > max - player_size):
            self.speed[current_coord] = self.speed[current_coord] * 0.4
            return max - player_size - pos
        if (pos + speed < 0):
            self.speed[current_coord] = self.speed[current_coord] * 0.4
            return -pos
        return speed