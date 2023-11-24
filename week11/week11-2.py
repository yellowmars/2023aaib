a,b=list(map(int,input().split()))
if a<0:a=-a
if b<0:b=-b
ans=0
for i in range(1,a+1):
	if a%i==0 and b%i==0:
		ans=i
print(ans,end='')