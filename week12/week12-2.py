#a=[1,1,2,3,5,8,13,21]
a=[1,1]
for i in range(2,30):  #課本第3章list的第3-6頁 .append()
  a.append(a[i-1]+a[i-2]) #利用 .append() 在最後面加一項

print(a)




a=[0]*100
a[0]=1
a[1]=1
for i in range(2,100):
  a[i]=a[i-1]+a[i-2]
print(a)