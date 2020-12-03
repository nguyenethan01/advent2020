with open('day2/data.txt') as f:
  data = f.readlines()

for i in range(len(data)):
  a,b,c = data[i].split(" ")
  data[i] = [a,b,c[:-1]]

for i in range(len(data)):
  lo,hi = data[i][0].split("-")
  lo = int(lo)
  hi = int(hi)
  data[i] = [lo,hi,data[i][1][:-1],data[i][2]]
data[999][3]+='x'


valid = 0
for i in data:
  if i[3][i[0]-1] == i[2] and i[3][i[1]-1] == i[2]:
      continue
  elif i[3][i[0]-1] == i[2] or i[3][i[1]-1] == i[2]:
    valid+=1

print(valid)
