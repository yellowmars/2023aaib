class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans=0
        #先用python把字串的迴圈寫出來
        N=len(s)
        j=0
        for i in range(N): #先用python把字串的迴圈寫出來
            maxCost-=abs(ord(s[i])-ord(t[i])) #毛毛蟲的頭i 
            while maxCost<0:  #預算不夠，便負的
                maxCost+=abs(ord(s[j])-ord(t[j])) #尾巴j
                j+=1 #尾巴j往右縮
            ans=max(ans,i-j+1) #頭i-尾j+1 就是毛毛蟲的長度
        return ans