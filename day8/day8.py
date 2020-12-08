with open('day8/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = data[i][:-1]
  

for i in range(len(data)):
  data[i] = data[i].split(' ')
  data[i][1] = int(data[i][1])


def terminates(data):
  seen = set()
  pos = 0
  ans = 0 
  while True:
    if pos in seen:
      return 0
    if pos == len(data):
      return (ans)

    seen.add(pos)

    curr = data[pos]
    if curr[0] == "acc":
      ans+= curr[1]
      pos+=1
    elif curr[0] == "jmp":
      pos+= curr[1]
    else:
      pos+=1
      

for i in range(len(data)):
  if data[i][0] == "jmp":
    new_data = data
    new_data[i][0] == "nop"
    curr_ans = terminates(new_data)
    print(curr_ans)
    if curr_ans != 0:
      print(curr_ans)
  elif data[i][0] == "nop":
    new_data = data
    new_data[i][0] == "jmp"
    curr_ans = terminates(new_data)
    print(curr_ans)
    if curr_ans !=0:
      print(curr_ans)
