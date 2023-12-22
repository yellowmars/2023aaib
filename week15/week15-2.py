 N=len(s) #長度
        zero=0
        one=0 #想找出全部的1
        for i in range(N): #如果是1，先全部加起來
        #現在就知道總共有幾個 one
            if s[i]=='1': one+=1
        #print('一開始的時候，都在右邊，統計結果','zero',zero,'one',one)
        ans=0
        for i in range(N-1): #要逐格去修正， 「吐出」一格，看他是多少，就修正
            if s[i]=='0':
                zero+=1
            if s[i]=='1':
                one-=1
            print('中間過程中，',zero,'one',one)
            ans=max(ans,zero+one)
        return ans