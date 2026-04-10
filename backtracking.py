"""
backtracking.py — Algorithme de résolution par backtracking simple (sans propagation)
"""


def backtracking(variables, domains, intersections):
    """
    Exploration DFS : assigne un mot à une variable, vérifie la compatibilité
    avec toutes les variables déjà assignées, revient en arrière si nécessaire.
    Aucune propagation de contraintes.
    Retourne : (solution: dict, nb_backtracks: int)
    """
    pass


def _is_consistent(var, word, assignment, intersections):
    """
    Vérifie que le mot proposé pour var est compatible avec toutes
    les variables déjà assignées (via les intersections).
    Retourne True si aucune contradiction n'est trouvée.
    """
    pass
