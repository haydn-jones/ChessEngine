import pyglet
from pyglet.image.codecs.png import PNGImageDecoder

class ResourceFactory():
    resources = {
        'board'   : "./resources/board.png",
        'text'    : "./resources/text.png",
        'numbers' : "./resources/numbers.png",

        'bishop_b': "./resources/black_bishop.png",
        'king_b'  : "./resources/black_king.png",
        'knight_b': "./resources/black_knight.png",
        'pawn_b'  : "./resources/black_pawn.png",
        'queen_b' : "./resources/black_queen.png",
        'rook_b'  : "./resources/black_rook.png",

        'bishop_w': "./resources/white_bishop.png",
        'king_w'  : "./resources/white_king.png",
        'knight_w': "./resources/white_knight.png",
        'pawn_w'  : "./resources/white_pawn.png",
        'queen_w' : "./resources/white_queen.png",
        'rook_w'  : "./resources/white_rook.png",
    }

    def __init__(self):
        self.images = {}
        self.load_images()

        self.scale = 1

    def set_scale(self, width, height):
        self.scale = int(height // self.images['board'].height)

    def load_images(self):
        for name, path in self.resources.items():
            self.images[name] = pyglet.image.load(path, decoder=PNGImageDecoder())
    
    def get_sprite(self, name):
        sprite = pyglet.sprite.Sprite(self.images[name])
        sprite.scale = self.scale

        return sprite
