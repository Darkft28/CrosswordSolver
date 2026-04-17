import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from solver import solve
from grid import load_grid, display_solution

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
LIMITE = 30


def benchmark(grid_file, dict_file, label):
    grille = load_grid(grid_file)
    print(f"\n=== Benchmark {label} ===")
    resultats = []
    for method in ['backtracking', 'fc', 'fc_mrv']:
        print(f"  {method}...", end=' ', flush=True)
        debut = time.time()
        solution, backtracks = solve(grid_file, dict_file, method, LIMITE)
        duree = time.time() - debut
        resolu = len(solution) > 0
        timeout = not resolu and duree >= LIMITE * 0.9
        print('OK' if resolu else (f'TIMEOUT (>{LIMITE}s)' if timeout else 'ECHEC'))
        resultats.append((method, backtracks, duree * 1000, resolu, timeout, solution))

    print(f"\n  {'Algorithme':<18} {'Backtracks':>12} {'Temps (ms)':>12} {'Résolu':>8}")
    print(f"  {'-'*52}")
    for method, bt, ms, ok, timeout, _ in resultats:
        res = 'Oui' if ok else (f'Non (>{LIMITE}s)' if timeout else 'Non')
        print(f"  {method:<18} {bt:>12} {ms:>12.1f} {res:>8}")

    for method, bt, ms, ok, timeout, solution in resultats:
        if method == 'fc_mrv' and ok:
            print(f"\n  Solution FC+MRV :")
            display_solution(grille, solution)


if __name__ == '__main__':
    benchmark(
        os.path.join(DATA_DIR, 'gridMP1.txt'),
        os.path.join(DATA_DIR, 'dictMP1.txt'),
        'MP1'
    )
    benchmark(
        os.path.join(DATA_DIR, 'gridMP2.txt'),
        os.path.join(DATA_DIR, 'dictMP2.txt'),
        'MP2'
    )
