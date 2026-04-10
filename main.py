"""
main.py — Point d'entrée : tests et tableau comparatif des 3 algorithmes
"""
import time
from solver import solve
from grid import load_grid, display_solution


def run_benchmark(grid_path, dict_path, label):
    """
    Lance les 3 algorithmes sur une paire grille/dictionnaire,
    affiche et retourne le tableau comparatif.
    """
    pass


def print_table(results):
    """
    Affiche un tableau comparatif :
    | Grille | Algorithme | Backtracks | Noeuds explorés | Temps (ms) |
    """
    pass


if __name__ == "__main__":
    run_benchmark("gridMP1.txt", "dictMP1.txt", "MP1")
    run_benchmark("gridMP2.txt", "dictMP2.txt", "MP2")
