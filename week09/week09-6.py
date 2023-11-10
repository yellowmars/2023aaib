a=input().split()
N=100
for i in range (N):
	a[i]=int(a[i])
for k in range(N):
	for i in range(1,N):
		if a[i]<a[i-1]:
			a[i],a[i-1]=a[i-1],a[i]
			
for i in range(N):
	print(a[i])
