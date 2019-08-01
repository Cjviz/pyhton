x,y = map(int,input().split())
for n in range(x,y):
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   if n == sum:
       print(n)
