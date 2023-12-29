a=input()
if a>='A' and a<='Z': ans='U'
elif a>='a' and a<='z': ans='L'
elif a>='0' and a<='9': ans='D'
else: ans='o'
print(ans,end='')