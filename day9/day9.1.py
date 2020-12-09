with open('day9/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = int(data[i][:-1])

data[len(data)-1] = int(data[len(data)-1])


for i in range(len(data)):
  for j in range(i+1, len(data)):
    if sum(data[i:j+1]) == 257342611:
      print(min(data[i:j+1])+max(data[i:j+1]))
      break