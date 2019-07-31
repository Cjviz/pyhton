a,b = map(str,input().split())
x = {}; y = {}
def is_isomorphic(a, b):
    if len(a) != len(b):
        return False
    else:
        for i, v in enumerate(a):
            if v in x and x[v] != b[i]:
                return False
            else:
                x[v] = b[i]
            if b[i] in y and y[b[i]] != v:
                return False
            else:
                y[b[i]] = v
        return True
z=is_isomorphic(a,b)
if (True==z):
  print("yes")
else:
  print("no")
