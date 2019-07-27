numb = int(input())
binary = '' 

while(numb):
 if(numb % 2 == 0):
  binary += '0'
 else:
  binary += '1'
 numb = numb//2

''.join(reversed(binary))

print(binary)
