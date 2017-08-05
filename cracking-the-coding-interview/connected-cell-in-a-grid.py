def get_biggest_region(grid):
    max_region = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_region = max(max_region, count_cells(grid, i, j))
    return max_region
    
def count_cells(grid, i, j):
    if not i in range(len(grid)) or not j in range(len(grid[0])):
        return 0
    if grid[i][j] == 0:
        return 0
    count = 1
    grid[i][j] = 0
    count += count_cells(grid, i + 1, j)
    count += count_cells(grid, i - 1, j)
    count += count_cells(grid, i, j + 1)
    count += count_cells(grid, i, j - 1)
    count += count_cells(grid, i + 1, j + 1)
    count += count_cells(grid, i - 1, j - 1)
    count += count_cells(grid, i - 1, j + 1)
    count += count_cells(grid, i + 1, j - 1)
    return count

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
