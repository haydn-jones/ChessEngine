from game import Game
from renderer import Renderer
from tqdm import trange
import pyglet

game = Game()
renderer = Renderer()

while not renderer.exited:
    move = renderer.get_move()
    if move != None:
        game.move(*move)

    renderer.run_loop(game)