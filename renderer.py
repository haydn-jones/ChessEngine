import pyglet
from pyglet.window import mouse
from resources.resources import ResourceFactory
import chess

class Renderer(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=720, height=720)
        self.exited = False

        self.resources = ResourceFactory()
        self.resources.set_scale(self.width, self.height)

        self.sprites = []
        self.load_sprites()

    def load_sprites(self):
        self.board = self.resources.get_sprite('board')

    def on_draw(self):
        self.clear()
        self.board.draw()

        for sprite in self.sprites:
            sprite.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')

    def on_close(self):
        self.exited = True
        self.close()

    def run_loop(self, board):
        pyglet.clock.tick()

        self.switch_to()
        self.dispatch_events()

        state = board.get_state()
        self.sprites = []
        for rank_index in range(7, -1, -1):
            for file_index in range(8):
                piece = state[rank_index][file_index]
                if piece == None:
                    continue

                sprite = self.resources.get_sprite(self.resources.piece_to_name(piece))

                sprite.x = file_index * self.resources.square_width * self.resources.scale + self.resources.square_width
                sprite.y = (7 - rank_index) * self.resources.square_width * self.resources.scale + self.resources.square_width
                self.sprites.append(sprite)

        self.dispatch_event('on_draw')
        self.flip()