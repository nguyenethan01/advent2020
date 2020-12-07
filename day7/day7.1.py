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
      storage["".join(i[:2])].add("".join(suffix[j:j+3]))

def count(bag):
  if len(storage[bag]) == 0:
    return 0
  return sum((int(i[0]) * (1+count(i[1:])) for i in storage[bag]))

print(count("shinygold"))
