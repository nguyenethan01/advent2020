from collections import defaultdict
with open('day10/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = int(data[i][:-1])

data[len(data)-1] = int(data[len(data)-1])

data = sorted(data)

storage = defaultdict(int)

storage[93] = 1
storage[92] = 1 
storage[91] = 1


def jumps(position):

  if position in storage:
    return storage[position]
  else:
    one = 0 
    two = 0
    three = 0
    if data[position+1] - data[position] <= 3:
      one = jumps(position+1)
    if data[position+2] - data[position] <= 3:
      two = jumps(position+2)
    if data[position+3] - data[position] <= 3:
      three = jumps(position+3)
  storage[position] = sum([one,two,three])
  return sum([one,two,three])

print(data)
print (sum([jumps(0),jumps(1),jumps(2)]))


  