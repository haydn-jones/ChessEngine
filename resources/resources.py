import pyglet
from pyglet.image.codecs.png import PNGImageDecoder
import chess

class ResourceFactory():
    resources = {
        'board'    : "./resources/board.png",
        'highlight': "./resources/highlight.png",

        'pawn_b'  : "./resources/pawn_b.png",
        'knight_b': "./resources/knight_b.png",
        'bishop_b': "./resources/bishop_b.png",
        'rook_b'  : "./resources/rook_b.png",
        'queen_b' : "./resources/queen_b.png",
        'king_b'  : "./resources/king_b.png",

        'pawn_w'  : "./resources/pawn_w.png",
        'knight_w': "./resources/knight_w.png",
        'bishop_w': "./resources/bishop_w.png",
        'rook_w'  : "./resources/rook_w.png",
        'queen_w' : "./resources/queen_w.png",
        'king_w'  : "./resources/king_w.png",
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