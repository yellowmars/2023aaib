s ="abcdabcd"
d={} 
for c in s:
  if c in d:
    d[c]=d[c]+1
  else:
    d[c]=1  
  print('現在看到的字母是', c,'字典是', d)  