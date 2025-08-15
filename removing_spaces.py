s=input()
res=""
for i in s:
    if i!=' ': #checks character in string is not space is space avoids space
        res+=i
print(res)
"""using built-in function
s=input()
res=s.replace(" ","")
print(res)
"""
