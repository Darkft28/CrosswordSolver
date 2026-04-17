import sys
import os
import threading
import time
import tkinter as tk
from tkinter import ttk
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from solver import solve
from grid import load_grid

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
TAILLE_CASE = 48


def dessiner_grille(canvas, grille):
    canvas.delete('all')
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            x1, y1 = j * TAILLE_CASE, i * TAILLE_CASE
            x2, y2 = x1 + TAILLE_CASE, y1 + TAILLE_CASE
            couleur = 'black' if grille[i][j] == 1 else 'white'
            canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline='gray')


def afficher_solution(canvas, grille, solution):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == 1:
                continue
            lettre = ''
            for (li, col, horizontal, longueur), mot in solution.items():
                if horizontal and li == i and col <= j < col + longueur:
                    lettre = mot[j - col]
                    break
                if not horizontal and col == j and li <= i < li + longueur:
                    lettre = mot[i - li]
                    break
            if lettre:
                cx = j * TAILLE_CASE + TAILLE_CASE // 2
                cy = i * TAILLE_CASE + TAILLE_CASE // 2
                canvas.create_text(cx, cy, text=lettre.upper(), font=('Arial', 18, 'bold'))


def lancer_interface():
    fenetre = tk.Tk()
    fenetre.title('Solveur de mots croisés')
    fenetre.resizable(False, False)

    panneau = tk.Frame(fenetre, padx=15, pady=15, bg='#f0f0f0')
    panneau.pack(side='left', fill='y')

    tk.Label(panneau, text='Solveur de mots croisés',
             font=('Arial', 13, 'bold'), bg='#f0f0f0').pack(pady=(0, 15))

    tk.Label(panneau, text='Grille :', bg='#f0f0f0').pack(anchor='w')
    choix_grille = tk.StringVar(value='MP1')
    tk.OptionMenu(panneau, choix_grille, 'MP1', 'MP2').pack(fill='x', pady=(2, 10))

    tk.Label(panneau, text='Algorithme :', bg='#f0f0f0').pack(anchor='w')
    choix_algo = tk.StringVar(value='fc_mrv')
    tk.OptionMenu(panneau, choix_algo, 'backtracking', 'fc', 'fc_mrv').pack(fill='x', pady=(2, 10))

    ttk.Separator(panneau).pack(fill='x', pady=10)

    btn_resoudre = tk.Button(panneau, text='▶ Résoudre',
                             font=('Arial', 11, 'bold'), bg='#4CAF50', fg='white', pady=6)
    btn_resoudre.pack(fill='x', pady=(0, 5))

    btn_effacer = tk.Button(panneau, text='Effacer', bg='#f44336', fg='white', pady=5)
    btn_effacer.pack(fill='x')

    ttk.Separator(panneau).pack(fill='x', pady=10)

    tk.Label(panneau, text='Résultats :', font=('Arial', 10, 'bold'), bg='#f0f0f0').pack(anchor='w')
    lbl_backtracks = tk.Label(panneau, text='Backtracks : —', bg='#f0f0f0', anchor='w')
    lbl_backtracks.pack(anchor='w')
    lbl_temps = tk.Label(panneau, text='Temps : —', bg='#f0f0f0', anchor='w')
    lbl_temps.pack(anchor='w')
    lbl_statut = tk.Label(panneau, text='', fg='gray', bg='#f0f0f0', font=('Arial', 9, 'italic'))
    lbl_statut.pack(pady=(8, 0))

    zone_grille = tk.Frame(fenetre, bg='white', padx=15, pady=15)
    zone_grille.pack(side='right')
    canvas = tk.Canvas(zone_grille, bg='white')
    canvas.pack()

    grille_courante = [None]

    def get_chemins():
        nom = choix_grille.get()
        return os.path.join(DATA_DIR, f'grid{nom}.txt'), os.path.join(DATA_DIR, f'dict{nom}.txt')

    def charger_grille():
        grid_path, _ = get_chemins()
        grille_courante[0] = load_grid(grid_path)
        largeur = len(grille_courante[0][0]) * TAILLE_CASE
        hauteur = len(grille_courante[0]) * TAILLE_CASE
        canvas.config(width=largeur, height=hauteur)
        dessiner_grille(canvas, grille_courante[0])
        lbl_backtracks.config(text='Backtracks : —')
        lbl_temps.config(text='Temps : —')
        lbl_statut.config(text='')

    choix_grille.trace('w', lambda *_: charger_grille())
    charger_grille()

    def resoudre():
        btn_resoudre.config(state='disabled', text='Calcul...')
        lbl_statut.config(text='Calcul en cours...', fg='gray')
        grid_path, dict_path = get_chemins()
        method = choix_algo.get()

        def calcul():
            debut = time.time()
            solution, backtracks = solve(grid_path, dict_path, method)
            duree = (time.time() - debut) * 1000

            def mise_a_jour():
                btn_resoudre.config(state='normal', text='▶ Résoudre')
                lbl_backtracks.config(text=f'Backtracks : {backtracks}')
                lbl_temps.config(text=f'Temps : {duree:.0f} ms')
                if solution:
                    lbl_statut.config(text='Résolu !', fg='green')
                    dessiner_grille(canvas, grille_courante[0])
                    afficher_solution(canvas, grille_courante[0], solution)
                else:
                    lbl_statut.config(text='Pas de solution trouvée.', fg='red')

            fenetre.after(0, mise_a_jour)

        threading.Thread(target=calcul, daemon=True).start()

    btn_resoudre.config(command=resoudre)
    btn_effacer.config(command=charger_grille)

    fenetre.mainloop()


if __name__ == '__main__':
    lancer_interface()
