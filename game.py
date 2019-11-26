import numpy as np
import chess

class Game():
    def __init__(self):
        self.board = chess.Board()
    
    def print_board(self):
        state = self.get_state()

        for rank in state:
            for piece in rank:
                if piece:
                    print(piece, end=" ")
                else:
                    print(".", end=" ")
            
            print("")
    
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
