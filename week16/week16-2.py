a=int(input())
for i in range(a):
	space=a-1-i
	for k in range(space):
		print(' ',end='')
	star=2*i+1
	for k in range(star):
		print('*',end='')		
	print()