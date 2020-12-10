from collections import defaultdict
with open('day10/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = int(data[i][:-1])

data[len(data)-1] = int(data[len(data)-1])

data = sorted(data)
print(data)


storage = defaultdict(int)

for i in range(len(data)-1):
  storage[data[i+1] - data[i]]+=1

print(storage)


