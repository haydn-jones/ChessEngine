from game import Game
from renderer import Renderer
from tqdm import trange
import pyglet

game = Game()
renderer = Renderer()

while not renderer.exited:
    renderer.run_loop(game)