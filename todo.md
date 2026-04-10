# Todo — Résolveur de mots croisés (Mini-projet 2ALGO)

> **Rendu :** dimanche 19 avril 2026 à 23h59
> **Groupe :** 2 étudiants (exceptionnellement 3 si promo impaire)
> **Livrable :** archive `.zip` contenant uniquement les codes sources

---

## contraintes globales

- [ ] Aucune librairie Python externe (numpy, constraint, etc.)
- [ ] Tkinter ou Pygame autorisés **uniquement** pour le bonus GUI
- [ ] Pas de deepcopy pour la restauration des domaines en forward checking
- [ ] Pas d'IA générative, pas de code trouvé sur internet

---

## 01 — chargement des données

- [ ] `load_grid(path)` — lit un fichier `.txt` (`_` = case blanche, `#` = case noire) et retourne une `list[list[int]]` (0 = blanc, 1 = noir)
- [ ] `load_dict(path)` — lit un fichier `.txt` (un mot par ligne) et retourne une `list[str]`

---

## 02 — modélisation des variables

- [ ] `get_variables(grid)` — parcourt la grille et retourne la liste des variables sous forme de quadruplets `(i, j, h, l)` :
  - `i` = indice ligne de la case de départ
  - `j` = indice colonne de la case de départ
  - `h` = `True` si horizontal, `False` si vertical
  - `l` = longueur du mot
  - Ne garder que les séquences de cases blanches de longueur ≥ 2

---

## 03 — domaines

- [ ] `get_domains(variables, words)` — retourne un `dict[tuple, list[str]]` où chaque variable est associée à la liste des mots du dictionnaire dont la longueur correspond à `l`

---

## 04 — contraintes (intersections)

- [ ] `get_intersections(variables)` — identifie toutes les paires de variables qui partagent une case (un mot horizontal et un mot vertical se croisent)
  - Retourne : `dict` ou liste de tuples `((var1, pos1), (var2, pos2))` où `pos1` et `pos2` sont les indices dans chaque mot correspondant à la case partagée
- [ ] `is_compatible(word1, pos1, word2, pos2)` — vérifie que `word1[pos1] == word2[pos2]`

---

## 05 — algorithme 1 : backtracking

- [ ] Exploration DFS : on assigne un mot à une variable, on vérifie la compatibilité avec toutes les variables déjà assignées, on revient en arrière si aucun mot ne convient
- [ ] Pas de propagation de contraintes
- [ ] Retourne : `(solution: dict, nb_backtracks: int)`

---

## 06 — algorithme 2 : forward checking

- [ ] À chaque assignation, propager : retirer des domaines des variables non assignées les mots incompatibles avec le mot venant d'être placé
- [ ] Restauration des domaines : **mémoriser uniquement les mots supprimés** (pas de deepcopy) — à chaque backtrack, réinsérer ces mots dans les domaines concernés
- [ ] Si un domaine devient vide → backtrack immédiat
- [ ] Retourne : `(solution: dict, nb_backtracks: int)`

---

## 07 — algorithme 3 : forward checking + MRV

- [ ] Identique au forward checking
- [ ] Ajout de l'heuristique **Minimum Remaining Values** : à chaque étape, choisir la variable non assignée dont le domaine courant est le plus petit
- [ ] Retourne : `(solution: dict, nb_backtracks: int)`

---

## 08 — interface commune

- [ ] Même signature d'appel pour les 3 algorithmes : `solve(grid, words, method)` avec `method` dans `{'backtracking', 'fc', 'fc_mrv'}`
- [ ] `display_solution(grid, solution)` — affiche la grille résolue en console

---

## 09 — tests et comparaison

- [ ] Appliquer les 3 algorithmes sur `gridMP1.txt` / `dictMP1.txt`
- [ ] Appliquer les 3 algorithmes sur `gridMP2.txt` / `dictMP2.txt`
- [ ] Vérifier que les 3 algorithmes trouvent la même solution unique
- [ ] Produire un tableau comparatif :

| Grille | Algorithme | Backtracks | Nœuds explorés | Temps (ms) |
|--------|------------|------------|----------------|------------|
| MP1    | Backtracking | | | |
| MP1    | Forward checking | | | |
| MP1    | FC + MRV | | | |
| MP2    | Backtracking | | | |
| MP2    | Forward checking | | | |
| MP2    | FC + MRV | | | |

- [ ] Analyser et commenter les complexités (commentaires dans le code ou fichier séparé)

---

## 10 — bonus (optionnels, uniquement si partie 2 entièrement réalisée)

- [ ] **GUI** : visualisation de la grille (cases noires / blanches) et de la solution avec Tkinter ou Pygame
- [ ] **Générateur de grilles** : à partir des dimensions et d'un dictionnaire, placer les cases noires pour obtenir une grille admettant exactement une solution *(question très délicate)*

---

## structure des fichiers suggérée

```
projet/
├── main.py               # point d'entrée, tests, comparaison
├── grid.py               # load_grid, get_variables, display_solution
├── dictionary.py         # load_dict, get_domains
├── constraints.py        # get_intersections, is_compatible
├── backtracking.py       # algorithme backtracking
├── forward_checking.py   # algorithme FC et FC+MRV
├── gridMP1.txt
├── dictMP1.txt
├── gridMP2.txt
├── dictMP2.txt
└── bonus/                # GUI et/ou générateur (optionnel)
```