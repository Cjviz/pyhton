x,y=map(int,input().split())
z=(input().split())[0:x] 
i=0
while i<y:
  m,n=map(int,input().split())
  i+=1
  print(min(z[m-1:n])) 
