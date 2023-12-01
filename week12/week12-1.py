a,b=list(map(int,input().split()))
def gcd(a,b):
	if a==0: return b
	if b==0: return a
	return gcd(b,a%b)
	
ans=gcd(a,b)
print(a//ans,b//ans)