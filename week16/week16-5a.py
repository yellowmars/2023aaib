a=int(input())
ans=0
for i in range(1,1001):
	if i*i==a:
		ans=i
print(ans,end='')