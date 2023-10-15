# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
#
# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。

# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。


from functools import cache

def dpDigitTypeCountSpecial(n:int)->int:
    s=str(n)

    @cache
    def f(i:int,mask:int,isLimit:bool,isNum:bool):
        if i==len(s): return int(isNum)

        res=0

        if not isNum:
            res=f(i+1,mask,False,False)

        low=0 if isNum else 1
        up= int(s[i]) if isLimit else 9

        for d in range(low,up+1):
            # 如果当前数字搞进去的数字d不受mask影响
            if mask >> d & 1 == 0:
                res += f(i+1,mask|(1<<d),isLimit and d==up,True)

        return res

    return f(0,0,True,False)


if __name__ == '__main__':
    n=2000000000
    print(dpDigitTypeCountSpecial(n))