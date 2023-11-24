#輾轉相除法(減法 大約就是 除法取餘數)
a=123456789012
b=987654321078
def gcd(a, b):
  print(a, b)
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)
ans=gcd(a, b)
print(ans) 