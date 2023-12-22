print('Enter two integers: ')
a,b=list(map(int,input().split()))
def gcd(a,b):
	if a==0: return b
	if b==0: return a
	return gcd(b,a%b)
print('The greatest common divisor of',a,'and',b,'is', gcd(a,b))