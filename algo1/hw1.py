rawfile = open('integerarray.txt', 'rb')
numbers = []

for n in rawfile:
  numbers.append(int(n))

print numbers[:5]
print numbers[-5:]

def mergeCount(A, B, D, inv):
  for i, d in enumerate(D):
    if A and not B:
      D[i] = A.pop(0)
    elif not A and B:
      D[i] = B.pop(0)
    elif A[0] < B[0]:
      D[i] = A.pop(0)
    else:
      D[i] = B.pop(0)
      inv = inv + len(A)
  return D, inv

def sortCount(array, n, inv):

  if n <= 1:
    return array, inv
  h = n / 2

  A = array[:h]
  B = array[h:]

  A, inv = sortCount(A, len(A), inv)
  B, inv = sortCount(B, len(B), inv)

  array, inv = mergeCount(A, B, array, inv)

  return array, inv

print sortCount(numbers, len(numbers), 0)[1]