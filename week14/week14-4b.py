a=int(input())
if a<=1500: ans=100
else: ans=100+(a-1500+249)//250*5
print(ans,end='')