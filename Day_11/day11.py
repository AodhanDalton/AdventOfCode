import time

grid = [list(line.strip()) for line in open('day11')]
#########################################################
#                  Part 1
#########################################################

# starting timer
start1 = time.time()

# method for calculating number of occupied seats
def count_occupied(grid, i, j, h, w):
    conditions = [
        i > 0 and j > 0 and grid[i - 1][j - 1] == '#', # NW
        i > 0 and grid[i - 1][j] == '#', # N
        i > 0 and j < w - 1 and grid[i - 1][j + 1] == '#', # NE
        j > 0 and grid[i][j - 1] == '#', # W
        j < w - 1 and grid[i][j + 1] == '#', # E
        i < h - 1 and j > 0 and grid[i + 1][j - 1] == '#', # SW
        i < h - 1 and grid[i + 1][j] == '#', # S
        i < h - 1 and j < w - 1 and grid[i + 1][j + 1] == '#', # SE
    ]
    return sum(int(c) for c in conditions)
    

def process_grid(grid):
    h = len(grid)
    w = len(grid[0])
    new_grid = []
    has_changed = False
    for i in range(h):
        new_row = []
        for j in range(w):
            if grid[i][j] == 'L' and count_occupied(grid, i, j, h, w) == 0:
                new_row.append('#')
                has_changed = True
            elif grid[i][j] == '#' and count_occupied(grid, i, j, h, w) >= 4:
                new_row.append('L')
                has_changed = True
            else:
                new_row.append(grid[i][j])
        new_grid.append(new_row)
    return new_grid, has_changed


while True:
    grid, has_changed = process_grid(grid)
    if not has_changed:
        break


print(f"Part 1: {sum(row.count('#') for row in grid)}Time: {time.time() - start1}")

#########################################################
#                  Part 2
#########################################################
start2 = time.time()

grid = [list(line.strip()) for line in open('day11')]
h = len(grid)
w = len(grid[0])
neighbors = [[list() for _ in range(w)] for _ in range(h)]

# east-west
for i, row in enumerate(grid):
    seats = [j for j, node in enumerate(row) if node != "."]
    for j1, j2 in zip(seats[:-1], seats[1:]):
        neighbors[i][j1].append((i, j2))
        neighbors[i][j2].append((i, j1))

# north-south
for j in range(w):
    seats = [i for i in range(h) if grid[i][j] != "."]
    for i1, i2 in zip(seats[:-1], seats[1:]):
        neighbors[i1][j].append((i2, j))
        neighbors[i2][j].append((i1, j))
               

all_coords = [(i, j) for j in range(w) for i in range(h) if grid[i][j] != '.']


# diagonal \
d = h - 1
while True:
    this_coord = [(u, v) for u, v in all_coords if u - v == d]

    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d -= 1


# diagonal /
d = 0
while True:
    this_coord = [(u, v) for u, v in all_coords if u + v == d]
    
    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d += 1


this_grid = [[v for v in row] for row in grid]

changed = True
while changed:
    new_grid = []
    changed = False
    for i, row in enumerate(this_grid):
        new_row = []
        for j, seat in enumerate(row):
            cur_val = this_grid[i][j]
            if cur_val == ".":
                new_row.append(".")
            else:    
                occupied = sum(int(this_grid[u][v] == '#') for u, v in neighbors[i][j])
                if occupied == 0 and cur_val == "L":
                    new_row.append("#")
                    changed = True
                elif occupied >= 5 and cur_val == "#":
                    new_row.append("L")
                    changed = True
                else:
                    new_row.append(cur_val)
        new_grid.append(new_row)
    this_grid = new_grid


print(f"Part 2: {[v for row in this_grid for v in row].count('#')}Time: {time.time() - start2}")