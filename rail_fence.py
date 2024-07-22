plaintext = "GOODMORNING"

lst = list(plaintext)

directionUp = True

first = []
second = []
third = []

for i in range(len(lst)):
  if i & 1 == 0:
    directionUp = not(directionUp)
  if directionUp == False and (i & 1 == 0) :
    first.append(lst[i])
  elif (directionUp == False or True) and (i & 1 == 1) :
    second.append(lst[i])
  elif i & 0 == 0:
    third.append(lst[i])

cipher = "".join(first+second+third)
print(cipher)

