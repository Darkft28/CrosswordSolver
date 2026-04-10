"""
grid.py — Chargement de la grille, extraction des variables, affichage
"""


def load_grid(path):
    """
    Lit un fichier .txt et retourne la grille sous forme de list[list[int]].
    '_' = case blanche (0), '#' = case noire (1)
    """
    grid = []
    with open(path, 'r') as f:
        for line in f:
            row = [1 if c == '#' else 0 for c in line.strip()]
            grid.append(row)
    return grid


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
    variables = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:  # Case blanche
                # Vérifier horizontal
                if j == 0 or grid[i][j-1] == 1:  # Début d'une séquence horizontale
                    length = 1
                    while j + length < len(grid[0]) and grid[i][j + length] == 0:
                        length += 1
                    if length >= 2:
                        variables.append((i, j, True, length))
                
                # Vérifier vertical
                if i == 0 or grid[i-1][j] == 1:  # Début d'une séquence verticale
                    length = 1
                    while i + length < len(grid) and grid[i + length][j] == 0:
                        length += 1
                    if length >= 2:
                        variables.append((i, j, False, length))
    return variables


def display_solution(grid, solution):
    """
    Affiche la grille résolue en console.
    solution : dict { (i, j, h, l) : mot }
    """
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                row += '#'
            else:
                lettre = '_'
                for (vi, vj, vh, vl), word in solution.items():
                    if vh and vi == i and vj <= j < vj + vl:
                        lettre = word[j - vj]
                        break
                    if not vh and vj == j and vi <= i < vi + vl:
                        lettre = word[i - vi]
                        break
                row += lettre
        print(row)