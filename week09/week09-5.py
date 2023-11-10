 #算平均的方法:(加起來)，在除(數量)
        N=len(salary)
        ans=(sum(salary)-max(salary)-min(salary))/(N-2)

        return ans