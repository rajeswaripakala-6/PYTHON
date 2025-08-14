s=input()
i=0
l=len(s)-1
flag=1
while i<l:
    if s[i] != s[l]:
        flag=0
        break
    i+=1
    l-=1
if flag==1:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
