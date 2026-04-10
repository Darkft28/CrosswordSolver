"""
grid.py — Chargement de la grille, extraction des variables, affichage
"""


def load_grid(path):
    """
    Lit un fichier .txt et retourne la grille sous forme de list[list[int]].
    '_' = case blanche (0), '#' = case noire (1)
    """
    pass


def get_variables(grid):
    """
    Parcourt la grille et retourne la liste des variables.
    Chaque variable est un quadruplet (i, j, h, l) :
      - i   : indice ligne de la case de départ
      - j   : indice colonne de la case de départ
      - h   : True si horizontal, False si vertical
      - l   : longueur du mot
    Seules les séquences de longueur >= 2 sont conservées.
    """
    pass


def display_solution(grid, solution):
    """
    Affiche la grille résolue en console.
    solution : dict { (i, j, h, l) : mot }
    """
    pass
