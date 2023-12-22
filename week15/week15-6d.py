a=list(map(int,input().split()))
ans=0
for b in a:
	if b>0: ans+=1
print(ans,end='')