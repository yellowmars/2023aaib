  table={}
        for num in nums:
            if num in table:
                table[num]+=1
            else:
                table[num]=1
        ans=[]
        for num in table:
            if table[num]==1:
                ans.append(num)
        return ans
        