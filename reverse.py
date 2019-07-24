reverse = ''
num = input()
for i in range(len(num), 0, -1):
    reverse += num[i-1]
print(int(reverse))
