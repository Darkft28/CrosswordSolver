import time


def backtracking(variables, domaines, intersections, limite=None):
    solution = {}
    nb_bt = [0]
    stop = [False]
    debut = time.time()

    def resoudre(i):
        if stop[0]:
            return False
        if i == len(variables):
            return True
        if limite and time.time() - debut > limite:
            stop[0] = True
            return False
        v = variables[i]
        for mot in domaines[v]:
            if stop[0]:
                return False
            if _consistant(v, mot, solution, intersections):
                solution[v] = mot
                if resoudre(i + 1):
                    return True
                del solution[v]
                nb_bt[0] += 1
        return False

    resoudre(0)
    return solution, nb_bt[0]


def _consistant(v, mot, solution, intersections):
    for (v1, p1), (v2, p2) in intersections:
        if v1 == v and v2 in solution and mot[p1] != solution[v2][p2]:
            return False
        if v2 == v and v1 in solution and mot[p2] != solution[v1][p1]:
            return False
    return True
