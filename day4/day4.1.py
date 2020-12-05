numValidPart1, numValidPart2 = 0, 0

optionalFields = set(['cid'])
requiredFields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
validFields = requiredFields.union(optionalFields)

def is4Digits(str):
  return len(str) == 4 and str.isdigit()

def validatePassport(passportDict):
  if set(passportDict.keys()).issuperset(requiredFields):

    birthYear = passportDict['byr']
    byrValid = is4Digits(birthYear) and int(birthYear) >= 1920 and int(birthYear) <= 2002


    issueYear = passportDict['iyr']
    iyrValid = is4Digits(issueYear) and int(issueYear) >= 2010 and int(issueYear) <= 2020


    expYear = passportDict['eyr']
    eyrValid = is4Digits(expYear) and int(expYear) >= 2020 and int(expYear) <= 2030


    hgtValue = passportDict['hgt']
    hgtUnit = hgtValue[-2:]
    hgtNum = hgtValue[:-2]
    hgtValid = (hgtUnit == 'cm' and int(hgtNum) >= 150 and int(hgtNum) <= 193) or (hgtUnit == 'in' and int(hgtNum) >= 59 and int(hgtNum) <= 76) and hgtNum.isnumeric()

    # hcl
    hairColor = passportDict['hcl']
    hclValid = True
    for i, hclStr in enumerate(hairColor): 
      if i == 0:
        hclValid = hclValid and hclStr[i] == '#'
      elif i < len(hclStr):
        hclValid = hclValid and hclStr[i].isalnum()
   

    eyeColor = passportDict['ecl']
    eclValid = eyeColor == 'amb' or eyeColor == 'blu' or eyeColor == 'brn' or eyeColor == 'gry' or eyeColor == 'grn' or eyeColor == 'hzl' or eyeColor == 'oth'


    passportID = passportDict['pid']
    pidValid = len(passportID) == 9 and passportID.isnumeric()

    return byrValid and iyrValid and eyrValid and hgtValid and hclValid and eclValid and pidValid
  return False

currPassportFields = set()
currPassportDict = {}

with open('day4/data.txt') as fp:
   line = fp.readline()
   while line:
     if line == '\n':
      
       if currPassportFields.issuperset(requiredFields):
         numValidPart1 = numValidPart1 + 1
       currPassportFields.clear()


       if validatePassport(currPassportDict):
         numValidPart2 = numValidPart2 + 1
       currPassportDict = {}
     else:
        tokens = line.split()
        for data in tokens:
          dataTokens = data.split(':')
          field, value = dataTokens[0], dataTokens[1]
          if field in validFields:
            currPassportFields.add(field)
            currPassportDict[field] = value
     line = fp.readline()

if currPassportFields.issuperset(requiredFields):
  numValidPart1 = numValidPart1 + 1
  
if validatePassport(currPassportDict):
  numValidPart2 = numValidPart2 + 1

print(f'Part 1\n{numValidPart1}\n\nPart 2\n{numValidPart2}')