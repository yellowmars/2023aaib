a,b=list(map(int,input().split()))
if a>b:
	a,b=b,a
for i in range(a,b+1):
	if i%5==0: print(i)