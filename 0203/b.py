h, w, n = map(int, input().split())
grid = [['.' for _ in range(w)] for _ in range(h)]
x, y , direction = 0, 0, 1
for _ in range(n):
  if grid[x][y] == '.':
    grid[x][y] = "#"
    direction = (direction + 1) % 4
  elif grid[x][y] == '#':
    grid[x][y] = "."
    direction = (direction - 1) % 4

  if direction == 0:
    y = (y - 1) % w
  elif direction == 1:
    x = (x - 1) % h
  elif direction == 2:
    y = (y + 1) % w
  elif direction == 3:
    x = (x + 1) % h
print('\n'.join([''.join(row) for row in grid]))
