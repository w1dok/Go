import argparse
import numpy as np

from dlgo.encoders import get_encoder_by_name
from dlgo import goboard_fast as goboard
from dlgo import mcts
from dlgo.utils import print_board, print_move

def generate_game(board_size, rounds, max_moves, temperature):
    boards, moves = [], [] 
    
    encoder = get_encoder_by_name('oneplane', board_size)
    
    game = goboard.GameState