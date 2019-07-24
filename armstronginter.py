x,y=map(int,input().split())
for n1 in range(x,y):
  sum=0
  temp=n1
  while(temp>0):
    sum=sum+(temp%10)**3
    temp=temp//10
  if(sum==n1):
    print(n1,end=" ")
