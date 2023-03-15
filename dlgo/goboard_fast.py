import copy
from dlgo.gotypes import Player, Point
from dlgo.scoring import computer_game_result
from dlgo import zobrist
from dlgo.utils import MoveAge

__all__ = [
    'Board',
    'GameState',
    'Move',
]

neighbot_tables = {}
corner_tables = {}

def init_neighbor_table(dim):
    rows, cols = dim
    new_table = {}
    for r in range(1 , rows + 1):
        for c in range(1, cols + 1):
            p = Point(row=r, col=c)
            full_neighbors = p.neighbors()
            true_neighbors = [
                n for n in full_neighbors
                if 1 <= n.row <= rows and 1 <= n.col <= cols]
            new_table[p] = true_neighbors
    neighbot_tables[dim] = new_table

def init_corner_table(dim):
    rows, cols = dim
    new_table = {}
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            p = Point(row=r, col=c)
            full_corners = [
                Point(row=p.row - 1, col=p.col - 1),
                Point(row=p.row - 1, col=p.col + 1),
                Point(row=p.row + 1, col=p.col - 1),
                Point(row=p.row + 1, col=p.col + 1),
            ]
            true_corners = [
                n for n in full_corners
                if 1 <= n.row <= rows and 1 <= n.col <= cols]
            new_table[p] = true_corners
        corner_tables[dim] = new_table
            
class IllegalMoveError(Exception):
    pass

class GoString():
    """Stones that are linked by a chain of connected stones of the
    same color.
    """
    def __init__(self, color, stones, liberties):
        self.color = color
        self.stones = frozenset(liberties)



























