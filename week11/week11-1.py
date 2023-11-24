a=30
b=45
ans=0
for i in range(1,a+1):
  if a%i==0 and b%i==0:
    print(i,'可以整除')
    ans=i #這個可以整除
print('最大公因數是',ans)