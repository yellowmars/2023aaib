a=list(map(int,input().split()))
N=len(a)
ans=0
for i in range(N-2):
	if a[i]==a[-1]:
		ans+=1
print(ans)