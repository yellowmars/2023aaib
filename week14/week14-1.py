 notAns=set()
        for a,b in paths:#先循第一輪
            notAns.add(a)#出發點不是答案

        for a,b in paths: #第二論，在檢查b
                if b not in notAns: #b不再出發裡，就是答案
                    return b #b不是「不是答案」