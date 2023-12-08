a=list(map(int,input().split()))
N=len(a)
for i in range(1,N):
	print(a[i]*a[i],end=',')
print()