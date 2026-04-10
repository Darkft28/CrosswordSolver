"""
constraints.py — Détection des intersections et vérification de compatibilité
"""


def get_intersections(variables):
    """
    Identifie toutes les paires de variables qui partagent une case
    (un mot horizontal croise un mot vertical).
    Retourne une liste de tuples : ((var1, pos1), (var2, pos2))
      - var1, var2 : variables (i, j, h, l)
      - pos1, pos2 : indices dans chaque mot correspondant à la case partagée
    """
    pass


def is_compatible(word1, pos1, word2, pos2):
    """
    Vérifie que word1[pos1] == word2[pos2].
    Retourne True si les deux mots sont compatibles à leur intersection.
    """
    pass
