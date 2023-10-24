# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
#
# 给定三个整数 n ,  k 和 target ，返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。
#
# 答案可能很大，你需要对 10^9 + 7 取模 。

# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。


from functools import cache


def numRollsToTarget(n:int,k:int,target:int)->int:
    MOD=10**9 + 7
    @cache
    def f(i,current_value):
        if current_value>target:return 0
        if i==n:return int(current_value==target)
        res = 0
        for d in range(1,k+1):
            res+=f(i+1,current_value+d)
        return res % MOD
    return f(0,0)


if __name__ == '__main__':
    n=30
    k=30
    target=500
    print(numRollsToTarget(n,k,target))