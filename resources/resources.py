import pyglet
from pyglet.image.codecs.png import PNGImageDecoder
import chess

class ResourceFactory():
    resources = {
        'board'   : "./resources/board.png",
        'text'    : "./resources/text.png",
        'numbers' : "./resources/numbers.png",

        'pawn_b'  : "./resources/black_pawn.png",
        'knight_b': "./resources/black_knight.png",
        'bishop_b': "./resources/black_bishop.png",
        'rook_b'  : "./resources/black_rook.png",
        'queen_b' : "./resources/black_queen.png",
        'king_b'  : "./resources/black_king.png",

        'pawn_w'  : "./resources/white_pawn.png",
        'knight_w': "./resources/white_knight.png",
        'bishop_w': "./resources/white_bishop.png",
        'rook_w'  : "./resources/white_rook.png",
        'queen_w' : "./resources/white_queen.png",
        'king_w'  : "./resources/white_king.png",
    }

    def __init__(self):
        self.images = {}
        self.load_images()

        self.scale = 1
        self.square_width = self.images['board'].height // 8

    def set_scale(self, width, height):
        self.scale = int(height // self.images['board'].height)

    def load_images(self):
        for name, path in self.resources.items():
            self.images[name] = pyglet.image.load(path, decoder=PNGImageDecoder())
    
    def get_sprite(self, name):
        sprite = pyglet.sprite.Sprite(self.images[name])
        sprite.scale = self.scale

        return sprite

    def piece_to_name(self, piece):
        name = chess.piece_name(piece.piece_type)
        color = "_w" if piece.color == chess.WHITE else "_b"

        return f"{name}{color}"