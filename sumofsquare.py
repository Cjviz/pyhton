    
y=int(input())
sum=0
while(y>0):
  r=x%10
  sum=sum+r*r
  y=y//10
print(sum)
