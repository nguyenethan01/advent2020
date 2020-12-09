with open('day9/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = int(data[i][:-1])

data[len(data)-1] = int(data[len(data)-1])


for i in range(25,len(data)):
  start = i - 25
  end = i - 1
  to_parse = sorted(data[start:end+1])
  lo = 0
  hi = len(to_parse)-1
  while lo <= hi:
    if lo == hi:
      print(data[i])
      break
    else:
      if to_parse[lo]+ to_parse[hi] < data[i]:
        lo+=1
        #print(lo)
      elif to_parse[lo] + to_parse[hi] > data[i]:
        hi-=1
        #print(hi)
      else:
        break
      
    
