 table={} #大括號: table[num]對應的次數
        for num in nums: #每個數字輪一次
            if num in table:#出現過的話
                    table[num]+=1 #次數加1
            else:
                    table[num]=1 #第一次出現
        #print(table)
        ans=0
        for num in table: #把table裡的數字輪一次
            if table[num]==2: #如果剛好出現2次
                ans=ans^num #把答案，照題目需求 混起來
        return ans        