def load_dict(path):
    with open(path, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def get_domains(variables, mots):
    return {v: [m for m in mots if len(m) == v[3]] for v in variables}
