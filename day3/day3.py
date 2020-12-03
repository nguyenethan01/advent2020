with open('day3/data.txt') as f:
  data = f.readlines()

for i in range(len(data)):
  if data[i][-1] == '\n':
    data[i] = data[i][:-1]

horizontal_max = len(data[1])-1
vertical_max = len(data)
vpos = 2
hpos = 1

ans = 0
while(vpos < vertical_max):
  if hpos > horizontal_max:
    hpos %= horizontal_max+1
  if data[vpos][hpos] == "#":
    ans+=1
  print(vpos,hpos,data[vpos][hpos])
  hpos+=1
  vpos+=2
  

print(ans)


