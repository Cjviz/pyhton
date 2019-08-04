string = ""
def isPalindrome(s):
    if s == s[::-1] :
        return True
s = input()
for idy, item in enumerate(s):
    for idx, item in enumerate(s):
        derp = s[idy:idx+1]
        if isPalindrome(derp) and (len(derp) > len(string)):
            string = derp
print(string)
