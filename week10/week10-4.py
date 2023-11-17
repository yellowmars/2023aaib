a=int(input())

if a<=2000:
	ans=100
else: #more than 2000
	ans=100
	more=a-2000 #多多少公尺
	ans+=more//500*5 #每500再跳1次5元
	if more%500:ans+=5 #有500的餘數的話再加5
  
print(ans)	



另解

a=int(input())

ans=100
if a>2000:
	ans+=(a-2000)//500*5
	if(a-2000)%500: ans+=5
	
print(ans)	