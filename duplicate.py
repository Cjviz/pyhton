s = input()
aa = [ ch  for i, ch in enumerate(s) if ch not in s[:i]]
print(''.join(aa))
