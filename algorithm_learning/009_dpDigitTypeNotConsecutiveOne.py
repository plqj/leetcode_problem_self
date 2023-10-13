# 给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。
from functools import cache


def dpDigitTypeNotConsecutiveOne(n:int) ->int:
    n_binary=bin(n)[2:] # 将数字n转化为二进制的字符串

    @cache
    def f(i:int,pre:bool,isLimit:bool):
        if i==len(n_binary):return 1 # 递归出口

        up = int(n_binary[i]) if isLimit else 1

        res=f(i+1, False, isLimit and up==0)

        if not pre and up==1:
            res += f(i+1,True,isLimit)
        return res

    return f(0,False,True)


if __name__ == '__main__':
    n=12
    print(dpDigitTypeNotConsecutiveOne(n))