"""
main.py — Point d'entrée : tests et tableau comparatif des 3 algorithmes
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from solver import solve
from grid import load_grid, display_solution

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def run_benchmark(grid_file, dict_file, label):
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
    run_benchmark(os.path.join(DATA_DIR, "gridMP1.txt"), os.path.join(DATA_DIR, "dictMP1.txt"), "MP1")
    run_benchmark(os.path.join(DATA_DIR, "gridMP2.txt"), os.path.join(DATA_DIR, "dictMP2.txt"), "MP2")
