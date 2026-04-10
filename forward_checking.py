"""
forward_checking.py — Algorithme FC et FC + heuristique MRV
"""


def forward_checking(variables, domains, intersections):
    """
    À chaque assignation, propage les contraintes : retire des domaines
    des variables non assignées les mots incompatibles avec le mot placé.
    Restauration par mémorisation des mots supprimés (pas de deepcopy).
    Backtrack immédiat si un domaine devient vide.
    Retourne : (solution: dict, nb_backtracks: int)
    """
    pass


def forward_checking_mrv(variables, domains, intersections):
    """
    Identique à forward_checking, avec l'heuristique MRV :
    à chaque étape, choisit la variable non assignée dont le domaine
    courant est le plus petit.
    Retourne : (solution: dict, nb_backtracks: int)
    """
    pass


def _propagate(var, word, domains, intersections, assignment):
    """
    Retire des domaines les mots incompatibles suite à l'assignation de `word` à `var`.
    Retourne la liste des (variable, mot_supprimé) pour permettre la restauration.
    Retourne None si un domaine devient vide (échec détecté).
    """
    pass


def _restore(pruned, domains):
    """
    Réinsère dans les domaines les mots précédemment supprimés.
    pruned : liste de (variable, mot_supprimé) retournée par _propagate.
    """
    pass


def _select_unassigned_mrv(variables, domains, assignment):
    """
    Sélectionne la variable non assignée avec le domaine le plus petit (MRV).
    """
    pass
