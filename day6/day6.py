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



ans = 0
for i in cleaned:
  storage  = set()
  for j in i:
    if j != "\n":
      storage.add(j)
  ans+= len(storage)

print(ans)

