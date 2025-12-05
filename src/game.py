from settings import *
from sprites import Player


class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Asteroid Shooter")
        self.textures = {}
        self.sounds = {}
        self.import_assets()
        self.player = Player(self.textures.get("spaceship"), Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 2))
        self.star_data = self.generate_starfield_data()

    def import_assets(self):
        self.textures = get_game_textures_map()
        self.sounds = get_game_sounds_map()

    def generate_starfield_data(self) -> list[tuple[Vector2, float]]:
        star_data = [
            (
                Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),
                uniform(0.4, 1.2)
            ) for i in range(30)
        ]
        return star_data

    def draw_starfield(self):
        for star, pos in self.star_data:
            draw_texture_ex(self.textures.get("star"), star, 0, pos, WHITE)

    def draw(self):
        self.draw_starfield()
        self.player.draw()

    def update(self, dtm):
        self.player.update(dtm)

    def run(self):
        while not window_should_close():
            dt = get_frame_time()
            self.update(dt)
            begin_drawing()
            clear_background(BG_COLOR)
            self.draw()
            end_drawing()
        close_window()


if __name__ == '__main__':
    game = Game()
    game.run()
