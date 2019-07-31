def cj(l):
    o="abcdefghijklmnopqrstuvwxyz"
    for g in o:
        if g not in l.lower():
            return False
    return True
lo=input()
if (cj(lo)==True):
    print("yes")
else:
    print("no")
