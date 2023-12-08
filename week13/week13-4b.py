a=int(input())
a1=a//1000*8
a2=a%1000//100*4
a3=a%100/10*2
a4=a%10
print(a1+a2+a3+a4)