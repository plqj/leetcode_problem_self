# 给你两个数字字符串 num1 和 num2 ，以及两个整数 max_sum 和 min_sum 。如果一个整数 x 满足以下条件，我们称它是一个好整数：
#
# num1 <= x <= num2
# min_sum <= digit_sum(x) <= max_sum.
# 请你返回好整数的数目。答案可能很大，请返回答案对 109 + 7 取余后的结果。
#
# 注意，digit_sum(x) 表示 x 各位数字之和。

# 输入：num1 = "1", num2 = "12", min_num = 1, max_num = 8
# 输出：11
# 解释：总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。

from functools import cache

def dpDigitTypeCountFourParameter(num1:str,num2:str,min_num:int,max_num:int)->int:
    MOD=10 ** 9 + 7
    def inner(s)->int:
        @cache
        def f(i:int,sum_cur:int,isLimit:bool,)->int:

            if sum_cur > max_num:return 0
            if i==len(s):return int(sum_cur>=min_num)

            res=0

            up=int(s[i]) if isLimit else 9

            for d in range(up+1):
                res += f(i+1,sum_cur+d,isLimit and d==up)

            return res%MOD

        return f(0,0,True)

    return inner(num2)-inner(num1)+int(min_num <= sum(map(int, num1)) <= max_num) %MOD


if __name__ == '__main__':
    num1 = "1"
    num2 = "12"
    min_num = 1
    max_num = 8
    print(dpDigitTypeCountFourParameter(num1,num2,min_num,max_num))

    # map函数的应用
    # map(func,iterable,...)
    # 将function应用于iterable的每一个元素，结果以map object的形式返回，是一个迭代器
    # 可以传很多个iterable，如果有额外的iterable参数，并行的从这些参数中取元素，并调用function
    # 如果一个iterable参数比另外的iterable参数要短，将以None扩展该参数元素
    # func可以是内置函数，def自定义函数，匿名函数
    # int(min_num <= sum(map(int, num1)) 检验num1是否是一个“好数”，将字符串的每一个元素（字符）用int()函数转变为数字后相加，然后和上界下界比较。若是一个好数，则为True，转为1后加到最终结果内