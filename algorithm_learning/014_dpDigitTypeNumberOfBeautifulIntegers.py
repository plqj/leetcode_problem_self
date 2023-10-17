# 给你正整数 low ，high 和 k 。
#
# 如果一个数满足以下两个条件，那么它是 美丽的 ：
#
# 偶数数位的数目与奇数数位的数目相同。
# 这个整数可以被 k 整除。
# 请你返回范围 [low, high] 中美丽整数的数目。

# 输入：low = 10, high = 20, k = 3
# 输出：2
# 解释：给定范围中有 2 个美丽数字：[12,18]
# - 12 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
# - 18 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
# 以下是一些不是美丽整数的例子：
# - 16 不是美丽整数，因为它不能被 k = 3 整除。
# - 15 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。
# 给定范围内总共有 2 个美丽整数。


from functools import cache

def dpDigitTypeNumberOfBeautifulIntegers(low:int,high:int,k:int)->int:

    def inner(s:str) -> int:
        @cache
        def f(i:int,k_divide:int,odd_num:int,even_num:int,isLimit:bool,isNum:bool):
            if i==len(s):return int(isNum and even_num==odd_num and k_divide==0)
            res=0
            if not isNum:res=f(i+1,k_divide,odd_num,even_num,False,False)

            low= 0 if isNum else 1
            up=int(s[i]) if isLimit else 9

            for d in range(low,up+1):
                if d%2==1:res+=f(i+1,(k_divide * 10 + d) % k,odd_num+1,even_num,isLimit and d==up,True)
                else:res+=f(i+1,(k_divide * 10 + d) % k,odd_num,even_num+1,isLimit and d==up,True)
            return res

        return f(0,0,0,0,True,False)

    return inner(str(high))-inner(str(low-1))



if __name__ == '__main__':
    low=10
    high=20
    k=3
    print(dpDigitTypeNumberOfBeautifulIntegers(low,high,k))