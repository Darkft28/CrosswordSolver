import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from grid import load_grid, get_variables
from dictionary import load_dict, get_domains
from constraints import get_intersections
from backtracking import backtracking
from forward_checking import forward_checking, forward_checking_mrv


def solve(grid_path, dict_path, method, limite=None):
    grille = load_grid(grid_path)
    variables = get_variables(grille)
    mots = load_dict(dict_path)
    domaines = get_domains(variables, mots)
    intersections = get_intersections(variables)
    if method == 'backtracking':
        return backtracking(variables, domaines, intersections, limite)
    elif method == 'fc':
        return forward_checking(variables, domaines, intersections, limite)
    elif method == 'fc_mrv':
        return forward_checking_mrv(variables, domaines, intersections, limite)
    return {}, 0
