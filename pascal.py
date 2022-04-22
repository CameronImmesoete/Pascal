# Retrying the Pascal problem

def PascalNChooseK(n, k):
  if n < 0 or k < 0 or k > n:
    return "Invalid"
  halfrow = PascalHelper(n)
  if len(halfrow) > k:
    return halfrow[k]
  return halfrow[n - k]

def PascalHelper(n):
  current = [1]
  last = [1]
  for countHeight in range(n + 1):
    last = current
    current = [1]
    for countWidth in range(1, len(last)):
      current += [last[countWidth - 1] + last[countWidth]]
    if countHeight > 0 and countHeight % 2 == 0:
      current += [last[len(last) - 1] * 2]
  return current

if __name__ == '__main__':
  print("N Choose K tests:")
  print("5 choose 2: " + str(PascalNChooseK(5, 2)))
  print("5 choose 3: " + str(PascalNChooseK(5, 3)))
  print("5 choose 6: " + str(PascalNChooseK(5, 3)))
  print("15 choose 4: " + str(PascalNChooseK(15, 4)) + " # if n > 13, factorial method would blow up")
  print("40 choose 30: " + str(PascalNChooseK(40, 30)) + " # if n > 13, factorial method would blow up")
  print("0 choose 0: " + str(PascalNChooseK(0, 0)))