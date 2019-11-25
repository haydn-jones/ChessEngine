import pyglet
from pyglet.image.codecs.png import PNGImageDecoder

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

def load_images():
    loaded = {}
    for name, path in resources.items():
        loaded[name] = pyglet.image.load(path, decoder=PNGImageDecoder())

    return loaded