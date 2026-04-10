"""
solver.py — Interface commune pour les 3 algorithmes
"""
from grid import load_grid, get_variables, display_solution
from dictionary import load_dict, get_domains
from constraints import get_intersections
from backtracking import backtracking
from forward_checking import forward_checking, forward_checking_mrv


def solve(grid_path, dict_path, method):
    """
    Point d'entrée unifié pour les 3 algorithmes.
    method : 'backtracking' | 'fc' | 'fc_mrv'
    Retourne : (solution: dict, nb_backtracks: int)
    """
    pass
