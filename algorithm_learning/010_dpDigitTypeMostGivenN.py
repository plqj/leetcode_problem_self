# 给定一个按 非递减顺序 排列的数字数组 digits 。
# 你可以用任意次数 digits[i] 来写的数字。
# 例如，如果 digits = ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。
#
# 返回 可以生成的小于或等于给定整数 n 的正整数的个数 。
#
# 输入：digits = ["1","3","5","7"], n = 100
# 输出：20
# 解释：
# 可写出的 20 个数字是：
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

from functools import cache

def dpDigitTypeMostGivenN(digits:list[str],n:int)->int:
    s=str(n)

    @cache
    def f(i:int,isLimit:bool,isNum:bool):
        # 递归出口
        if i == len(s):return int(isNum)

        res=0

        if not isNum:
            res=f(i+1,False,False) # 上一位不填了，所以这一位任意数字都不会越界，当前还不是数字

        up=s[i] if isLimit else "9"

        for d in digits:
            if d > up: break
            res += f(i+1,isLimit and d == up,True)
        return res

    return f(0,True,False)


if __name__ == '__main__':
    digits=["1","3","5","7"]
    n=100
    print(dpDigitTypeMostGivenN(digits,n))