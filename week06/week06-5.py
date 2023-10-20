    d={}
        for c in s:
            if c in d:
                d[c]=d[c]+1
            else:
                 d[c]=1
    print(d) #可以印印看，字母出現在次數統計解果
                  
    for c in t:
        if c not in d:
            return c #竟然沒出現過，就是他
               
        if d[c]==0: #字母用完了，不夠用，就是他
                
              return c #找到多出來的字母
        else:
            d[c]=d[c]-1 #就簡單地檢掉1
        
        