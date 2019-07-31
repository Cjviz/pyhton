def cj(a):
    if(a=="I"):
        return 1
    if(a=="V"):
        return 5
    if(a=="X"):
        return 10
    if(a=="P"):
        return 50
    if(a=="G"):
        return 100
    if(a=="R"):
        return 500
    if(a=="L"):
        return 1000
    return -1
def cj(m):
    res=0
    p=0
    while(p<len(m)):
        l1=cj(m[p])
        if(p+1<len(m)):
            l2=cj(m[p+1])
            if(l1>=l2):
                res=res+l1
                p=p+1
            else:
                res=res+l2-l1
                p+=2
        else:
            res=res+l1
            p=p+1
    print(res)
n=input()
cj(str(n))
