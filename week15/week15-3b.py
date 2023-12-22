ans=0
while True:
	print('Enter an integer ( 999 to end ): ')
	a=int(input())
	if a==999: break
	ans+=a
print('The total is:',ans,end='')