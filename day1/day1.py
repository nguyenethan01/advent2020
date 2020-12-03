#read data 
with open('day1/data.txt') as f:
  data = f.readlines()

for i in range(len(data)):
  data[i] = int(data[i])

data.sort()

for i in range(len(data)-2):
  want = 2020-data[i]
  low = i+1
  high = len(data)-1
  while(low != high):
    if data[low] + data[high] == want:
      print(data[low] * data[high] * data[i])
      break
    elif data[low] + data[high] < want:
      low+=1
    else:
      high-=1


