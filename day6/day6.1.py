from collections import defaultdict
with open('day6/data.txt') as f:
  data = f.readlines()
print(data)

cleaned = []
curr = ""
for i in data:
  if i!= "\n":
    curr+=i
  else:
    cleaned.append(curr)
    curr = ""
cleaned.append(curr)
cleaned[len(cleaned)-1] += '\n'

ans = 0

for i in cleaned:
  curr_len = 0
  storage = defaultdict(int)
  for j in i:
    if j != "\n":
      storage[j]+=1
    else:
      curr_len +=1
  curr_count = 0
  for x in storage.values():
    if x == curr_len:
      curr_count+=1
  ans+= curr_count
    
print(ans)