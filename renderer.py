import pyglet
from pyglet.window import mouse
from resources.resources import ResourceFactory
import chess

class Renderer(pyglet.window.Window):
    def __init__(self):
        super().__init__(width=768, height=768)

        self.exited = False

        self.resources = ResourceFactory()
        self.resources.set_scale(self.width, self.height)

        self.board = None
        self.highlight = None
        self.sprites = []
        self.load_sprites()

        self.selected_square = (-1, -1)
        
    def load_sprites(self):
        self.board = self.resources.get_sprite('board')
        self.highlight = self.resources.get_sprite('highlight')

    def on_draw(self):
        self.clear()
        self.board.draw()
        self.highlight.draw()

        for sprite in self.sprites:
            sprite.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            col = x // (self.resources.scale * self.resources.square_width)
            row = y // (self.resources.scale * self.resources.square_width)

            if self.selected_square == (row, col):
                row = -1
                col = -1

            self.selected_square = (row, col)
            
            self.highlight.x = col * self.resources.scale * self.resources.square_width
            self.highlight.y = row * self.resources.scale * self.resources.square_width

    def on_close(self):
        self.exited = True
        self.close()

    def run_loop(self, board):
        pyglet.clock.tick()

        self.switch_to()
        self.dispatch_events()

        self.sprites = []
        self.draw_board(board)

        self.dispatch_event('on_draw')
        self.flip()

    def draw_board(self, board):
        state = board.get_state()
        for rank_index in range(7, -1, -1):
            for file_index in range(8):
                piece = state[rank_index][file_index]
                if piece == None:
                    continue

                sprite = self.resources.get_sprite(self.resources.piece_to_name(piece))

                sprite.x = file_index * self.resources.square_width * self.resources.scale
                sprite.y = (7 - rank_index) * self.resources.square_width * self.resources.scale
                
                self.sprites.append(sprite)
