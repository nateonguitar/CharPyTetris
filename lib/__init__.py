import datetime

import charpy
from numpy.core.fromnumeric import shape
from pynput import keyboard

from lib.shape import *
from lib.core_game import CoreGame
from lib.start_screen import StartScreen
from lib.end_screen import EndScreen

class TetrisGame(charpy.Game):


    def __init__(self):
        super().__init__()
        self.deltatime : datetime.timedelta = None
        self.set_on_keydown(self.on_key_down)
        self.set_on_keyup(self.on_key_up)
        self.core_game = CoreGame()
        self.start_screen = StartScreen()
        self.end_screen= EndScreen()
        self.game_mode = self.start_screen
        self.run()
    

    def draw(self):
        self.game_mode.draw(self.screen)
        super().draw()


    def update(self, deltatime: datetime.timedelta):
        self.deltatime = deltatime
        self.game_mode.update(deltatime)


    def on_key_down(self, key: keyboard.Key):
        self.game_mode.on_key_down(key)


    def on_key_up(self, key: keyboard.Key):
        self.game_mode.on_key_up(key)

    
    def start_core_game(self):
        self.game_mode = self.core_game


    def end_core_game(self, score: int, got_high_score: bool):
        self.game_mode = self.end_screen
