from os.path import join
from pathlib import Path
from random import randint, choice,uniform
from pyray import *
from raylib import *

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
BG_COLOR = (15, 10, 25, 255)
PLAYER_SPEED = 500
LASER_SPEED = 600
METEOR_SPEED_RANGE = (100, 300)
METEOR_TIMER_DURATION = 0.4
DISCARD_LIMIT = 300

GAME_ASSETS_PATH = "../assets"

def get_game_music_stream(name):
    return load_music_stream(join(GAME_ASSETS_PATH,"music", name))

def get_game_sounds_map():
    loc = Path(join(GAME_ASSETS_PATH, "audio"))
    return {
        p.stem:
            load_sound(str(p))
            for p in loc.glob("*.wav")
    }


def get_game_textures_map():
    loc = Path(join(GAME_ASSETS_PATH, "images"))
    return {
        p.stem: (
            load_texture(str(p))
        )
        for p in loc.glob("*.png")
    }


def unload_game_sounds():
    for sound in get_game_sounds_map().values():
          unload_sound(sound)

def unload_game_textures():
    for texture in get_game_textures_map().values():
        unload_texture(texture)


def get_font(full_name):
    return load_font(join(GAME_ASSETS_PATH, "font", full_name))
