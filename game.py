import numpy as np
import chess

class Game():
    def __init__(self):
        self.board = chess.Board()
    
    def print_board(self):
        print(self.board)
    
    def get_state(self):
        state = []
        for rank_index in range(7, -1, -1):
            rank = []
            for file_index in range(8):
                square_index = chess.square(file_index, rank_index)
                piece = self.board.piece_at(square_index)

                rank.append(piece)

            state.append(rank)

        return state

    def move(self, from_square, to_square):
        from_square = f"{chess.FILE_NAMES[from_square[1]]}{chess.RANK_NAMES[from_square[0]]}"
        to_square   = f"{chess.FILE_NAMES[to_square[1]]}{chess.RANK_NAMES[to_square[0]]}"
    
        try:
            self.board.push_uci(f"{from_square}{to_square}")
        except:
            print("Illegal move / Not your turn!")