from settings import *


class Sprite:
    def __init__(self, texture, position, speed, direction):
        self.texture = texture
        self.position = position
        self.speed = speed
        self.direction = direction
        self.size = Vector2(texture.width, texture.height)

    def update(self, delta_time):
        pass

    def draw(self):
        draw_texture_v(self.texture, self.position, WHITE)

    def move(self, dtm):
        self.position.x += self.direction.x * dtm * self.speed
        self.position.y += self.direction.y * dtm * self.speed


class Player(Sprite):
    def __init__(self, texture, position, action_callback=None):
        super().__init__(texture, position, PLAYER_SPEED, Vector2())
        self.action_callback = action_callback

    def input(self):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.direction = Vector2Normalize(self.direction)

        if is_key_pressed(KEY_SPACE):
            self.action_callback(Vector2((self.position.x + self.size.x/ 2)-5, self.position.y - 20))

        self.position.x = clamp(self.position.x, 0, WINDOW_WIDTH - self.size.x)
        self.position.y = clamp(self.position.y, 0, WINDOW_HEIGHT - self.size.y)

    def update(self, delta_time):
        self.input()
        self.move(delta_time)


# ------------------------------------------------------------------------------------
class Lazer(Sprite):
    def __init__(self, texture, position):
        super().__init__(texture, position, LASER_SPEED, Vector2(0, -1))

    def update(self, delta_time):
        self.move(delta_time)
