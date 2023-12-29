a=list(map(int,input().split()))
a.sort()
ans=a[2]*100+a[1]*10+a[0]+1
print(ans,end='')