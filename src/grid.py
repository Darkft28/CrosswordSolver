def load_grid(path):
    grid = []
    with open(path) as f:
        for line in f:
            row = [1 if c == '#' else 0 for c in line.strip()]
            if row:
                grid.append(row)
    return grid


def get_variables(grid):
    variables = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                if j == 0 or grid[i][j-1] == 1:
                    l = 0
                    while j + l < len(grid[0]) and grid[i][j+l] == 0:
                        l += 1
                    if l >= 2:
                        variables.append((i, j, True, l))
                if i == 0 or grid[i-1][j] == 1:
                    l = 0
                    while i + l < len(grid) and grid[i+l][j] == 0:
                        l += 1
                    if l >= 2:
                        variables.append((i, j, False, l))
    return variables


def display_solution(grid, solution):
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                row += '#'
            else:
                c = '?'
                for (vi, vj, vh, vl), mot in solution.items():
                    if vh and vi == i and vj <= j < vj + vl:
                        c = mot[j - vj]
                        break
                    if not vh and vj == j and vi <= i < vi + vl:
                        c = mot[i - vi]
                        break
                row += c
        print(row)
