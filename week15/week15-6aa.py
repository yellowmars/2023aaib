a=input()
N=len(a)
bad=0
for i in range(N):
	if a[i]!=a[N-1-i]:
		bad+=1
if bad==0: print('YES',end='')
else: print('NO',end='')