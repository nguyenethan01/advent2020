import 
with open('day14/data.txt') as f:
  data = f.readlines()

for i in range(len(data)-1):
  data[i] = data[i][:-1]


get_bin = lambda x, n: format(x, 'b').zfill(n)

storage = {}

for i in data:
  if i.split(' ')[0] == 'mask':
    mask = i.split(' ')[2]
  else:
    answers = []
    curr =i.split(' ')
    location = get_bin(int(curr[0][4:-1]),36)
    value = int(curr[2])
    answers.append("")
    for i in range(len(mask)):
      if mask[i]== '1':
        for j in range(len(answers)):
          answers[j] += '1'
      elif mask[i] == '0':
        answers2 = [_ for _ in answers]
        answers = zip(answers,answers2)
        for j in range(len(answers)):
          if j %2 == 1:
            answers[j] +='1'
          else:
            answers[j] += '0'
      else:
        for j in range(len(answers)):
          answers[j]+= location[j]
    for thingy in answers:
      storage[int(thingy,2)] = value
  

print(sum(storage.values()))


