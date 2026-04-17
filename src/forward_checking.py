import time


def forward_checking(variables, domaines, intersections, limite=None):
    solution = {}
    nb_bt = [0]
    stop = [False]
    debut = time.time()

    def resoudre(restantes):
        if stop[0]:
            return False
        if not restantes:
            return True
        if limite and time.time() - debut > limite:
            stop[0] = True
            return False
        v = restantes[0]
        for mot in list(domaines[v]):
            if stop[0]:
                return False
            solution[v] = mot
            supprimes = _propager(v, mot, domaines, intersections, solution)
            if supprimes is not None:
                if resoudre(restantes[1:]):
                    return True
                _restaurer(supprimes, domaines)
            del solution[v]
            nb_bt[0] += 1
        return False

    resoudre(list(variables))
    return solution, nb_bt[0]


def forward_checking_mrv(variables, domaines, intersections, limite=None):
    solution = {}
    nb_bt = [0]
    stop = [False]
    debut = time.time()

    def resoudre(restantes):
        if stop[0]:
            return False
        if not restantes:
            return True
        if limite and time.time() - debut > limite:
            stop[0] = True
            return False
        v = min(restantes, key=lambda x: len(domaines[x]))
        autres = [u for u in restantes if u != v]
        for mot in list(domaines[v]):
            if stop[0]:
                return False
            solution[v] = mot
            supprimes = _propager(v, mot, domaines, intersections, solution)
            if supprimes is not None:
                if resoudre(autres):
                    return True
                _restaurer(supprimes, domaines)
            del solution[v]
            nb_bt[0] += 1
        return False

    resoudre(list(variables))
    return solution, nb_bt[0]


def _propager(v, mot, domaines, intersections, solution):
    supprimes = []
    for (v1, p1), (v2, p2) in intersections:
        if v1 == v:
            voisine, pm, pv = v2, p1, p2
        elif v2 == v:
            voisine, pm, pv = v1, p2, p1
        else:
            continue
        if voisine in solution:
            continue
        lettre = mot[pm]
        for m in list(domaines[voisine]):
            if m[pv] != lettre:
                domaines[voisine].remove(m)
                supprimes.append((voisine, m))
        if not domaines[voisine]:
            _restaurer(supprimes, domaines)
            return None
    return supprimes


def _restaurer(supprimes, domaines):
    for v, m in supprimes:
        domaines[v].append(m)
