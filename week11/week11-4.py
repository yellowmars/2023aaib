a,b=list(map(int,input().split()))
if a<0:a=-a
if b<0:b=-b
def gcd(a,b):
	if a==0: return b
	if b==0: return a
	return gcd(b,a%b)
ans=gcd(a,b)
print(ans,end='')