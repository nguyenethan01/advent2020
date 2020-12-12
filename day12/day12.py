from collections import defaultdict
with open('day12/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = data[i][:-1]

x, y = 0, 0
dx, dy = 10, 1
for i in data:
    dir, number = i[0], int(i[1:])
    if dir == 'N':
        dy += number
    elif dir == 'S':
        dy -= number
    elif dir == 'W':
        dx -= number
    elif dir == 'E':
        dx += number
    elif dir == 'L':
        for i in range(number // 90):
            dx, dy = -dy, dx
    elif dir == 'R':
        for i in range(number // 90):
            dx, dy = dy, -dx
    else:
        x += dx * number
        y += dy * number
print(abs(x) + abs(y))
