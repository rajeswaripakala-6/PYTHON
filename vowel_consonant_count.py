s=input()
vowels='aeiouAEIOU'
v_count=0
c_count=0
for i in s:
    if i.isalpha():#if alpha numeric present to count alpha numeric we use this//
        if i in vowels:
            v_count+=1
        else:
            c_count+=1
print("count of vowels:",v_count)
print("count of consonants:",c_count)

    
