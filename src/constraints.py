def get_intersections(variables):
    intersections = []
    for a in range(len(variables)):
        for b in range(a + 1, len(variables)):
            v1, v2 = variables[a], variables[b]
            if v1[2] == v2[2]:
                continue
            vh, vv = (v1, v2) if v1[2] else (v2, v1)
            ih, jh, lh = vh[0], vh[1], vh[3]
            iv, jv, lv = vv[0], vv[1], vv[3]
            if iv <= ih < iv + lv and jh <= jv < jh + lh:
                intersections.append(((vh, jv - jh), (vv, ih - iv)))
    return intersections
