with open('day4/data.txt') as f:
  data = f.readlines()

cleaned = []
curr = ""
for i in data:
  if i == "\n":
    cleaned.append(curr)
    curr = ""
  else:
    curr+=i

for i in range(len(cleaned)):
  cleaned[i] = cleaned[i].split()


correct1 = set({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"})
correct2 = set({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})

valid = 0

for i in cleaned:
  contains = set()
  for j in i:
    contains.add(j[:3])
  
  if contains == correct1 or contains == correct2:
    valid+=1
    print(contains)

print(valid)
  


