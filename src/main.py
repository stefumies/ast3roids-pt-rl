from settings import *
from game_timer import Timer
from sprites import Player, Lazer


class Game:
    def __init__(self):
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Asteroid Shooter")
        init_audio_device()
        self.textures = {}
        self.sounds = {}
        self.import_assets()
        self.lazers = []
        self.meteor_timer = Timer(METEOR_TIMER_DURATION, True, True, self.generate_meteor)
        self.player = Player(self.textures.get("spaceship"), Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 2),
                             self.fire_lazer)
        self.star_data = self.generate_starfield_data()

    def import_assets(self):
        self.textures = get_game_textures_map()
        self.sounds = get_game_sounds_map()

    @staticmethod
    def generate_starfield_data() -> list[tuple[Vector2, float]]:
        star_data = [
            (
                Vector2(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),
                uniform(0.5, 1.2)
            ) for _ in range(30)
        ]
        return star_data

    def draw_starfield(self):
        for star, pos in self.star_data:
            draw_texture_ex(self.textures.get("star"), star, 0, pos, WHITE)

    def generate_meteor(self):
        print("Generating Meteor")

    def fire_lazer(self, pos):
        self.lazers.append(Lazer(self.textures.get("laser"), pos))
        play_sound(self.sounds.get("laser",(None, None)))

    def discard_sprites(self):
        self.lazers = [lazer for lazer in self.lazers if not lazer.discard]

    def update(self):
        dt = get_frame_time()
        self.meteor_timer.update()
        self.player.update(dt)
        self.discard_sprites()
        for lazer in self.lazers:
            lazer.update(dt)

    def draw(self):
        begin_drawing()
        clear_background(BG_COLOR)
        self.draw_starfield()
        self.player.draw()
        for lazer in self.lazers:
            lazer.draw()
        end_drawing()

    def run(self):
        while not window_should_close():
            self.update()
            self.draw()
        unload_game_sounds()
        unload_game_textures()
        close_window()


if __name__ == '__main__':
    game = Game()
    game.run()
