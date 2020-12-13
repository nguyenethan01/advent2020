from collections import defaultdict
with open('day13/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = data[i][:-1]


data[0] = int(data[0])

nums = []
for i in data[1].split(','):
  try:
    nums.append(int(i))
  except:
    pass



pos = 100000000000000
print(pos)
print(nums)



reached= True
seen = []

while reached:
  for bus in nums:
    if pos % bus == 0:
      if bus == 19:
        seen = [19,]
      elif bus == 17:
        if seen.append(17) == [19, 41, 37, 787, 13, 23, 29, 571, 17]:
          print(pos)
          break
      seen.append(bus)

  pos+=1