a=input()
for c in a:
	if c.isupper():
		print(c.lower(),end='')
	elif c.islower():
		print(c.upper(),end='')
	else:
		print(c,end='')
print()