
with open('day7/data.txt') as f:
  data = f.readlines()

storage = {}

for i in data:
  i = i.split(" ")
  suffix = i[4:]
  if suffix == ['no', 'other', 'bags.\n']:
    storage["".join(i[:2])] = set()
  for j in range(len(suffix)):
    if suffix[j].isnumeric():
      if "".join(i[:2]) not in storage:
        storage["".join(i[:2])] = set()
      storage["".join(i[:2])].add("".join(suffix[j+1:j+3]))
  

for i in storage.items():
  print(i)


def find(bag):
  '''finds if shiny gold can be reached form bag'''
  seen.add(bag)
  if any("shinygold" == i for i in storage[bag]):
    return True

  for child in storage[bag]:
    if child not in seen:
      if find(child):
        return True

  return False


ans = 0


for i in storage.keys():
  seen = set()
  if find(i):
    ans+=1
  

print(ans)
  
