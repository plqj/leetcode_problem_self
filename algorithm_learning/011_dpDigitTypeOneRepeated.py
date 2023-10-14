# 给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
#
# 输入：n = 100
# 输出：10
# 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。


from functools import cache

# 采用正难则反的思路
def dpDigitTypeOneConsecutive(n:int) -> int:
    s=str(n)

    @cache
    def f(i:int,mask,isLimit:bool,isNum:bool) -> int:
        # 递归出口
        if i == len(s):return int(isNum) # 合法数字

        res=0

        if not isNum:
            res=f(i+1,mask,False,False)

        low=0 if isNum else 1 # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        up=int(s[i]) if isLimit else 9

        for d in range(low,up+1):
            if mask >> d & 1 == 0: # mask里的第d个字符为零（d不在已经出现过的数字集合中
                res+=f(i+1,mask|(1<<d),isLimit and d==up,True)

        return res

    return n-f(0,0,True,False)


if __name__ == '__main__':
    n=11
    print(dpDigitTypeOneConsecutive(n))