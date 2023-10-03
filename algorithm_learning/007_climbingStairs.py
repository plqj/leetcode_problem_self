# 爬楼梯
#
# 给定一个共有 𝑛 阶的楼梯，你每步可以上 1 阶或者 2 阶，请问有多少种方案可以爬到楼顶。

class Back():
    def __init__(self,n):
        self.n=n # stairs
        self.choices=[1,2]
        self.state=0
        self.paths=[] # sequence of moving
        self.path=[] # stores the path
        self.count=0 # how many ways

    def backtrack(self,state):
        if state == self.n:
            self.paths.append(self.path[:])
            self.count+=1
            return

        for choice in self.choices:
            if state+choice>self.n: # 先剪枝
                break
            self.path.append(choice)
            self.backtrack(state+choice)
            self.path.pop()

        return self.count,self.paths


class Direct():
    # 考虑原问题为 dp[i], 到达dp[i]前必须要先经历到dp[i-1]或者dp[i-2]，然后直接一步到位。那么得到公式dp[i]=dp[i-1]+dp[i-2]，所以写递归
    def iteration(self,i):
        if i==1 or i==2:
            return i

        count=self.iteration(i-1)+self.iteration(i-2)

        return count


class Direct_Memory():
    def __init__(self,n):
        self.n=n
        self.mem=[-1]*(self.n+1)

    def iteration_with_memory(self,i):
        if i==1 or i==2:
            return i

        if self.mem[i] != -1:
            # 引入了记忆单元，之前计算过的内容直接读取即可，牺牲了内存空间，但是时间复杂度从指数阶降到了线性阶
            return self.mem[i]

        count = self.iteration_with_memory(i - 1) + self.iteration_with_memory(i - 2)
        self.mem[i] = count
        return count


class DP():
    def __init__(self,n):
        self.n=n

    def dp(self,i):
        if i == 1 or i ==2:
            return i

        # 初始化 dp 表，用于存储子问题的解
        dp = [0] * (n + 1)
        # 初始状态：预设最小子问题的解
        dp[1], dp[2] = 1, 2

        # 状态转移：从较小子问题逐步求解较大子问题
        for j in range(3, i + 1):
            dp[j] = dp[j - 1] + dp[j - 2]

        return dp[i]


class DP_memoryfree():
    def __init__(self,n):
        self.n=n

    def dp(self,i):
        if i == 1 or i ==2:
            return i

        # 其实不需要用dp数组储存结果，只需要两个数滚动前进即可，空间复杂度降到常数阶，时间复杂度为线性阶
        a, b = 1, 2

        for _ in range(3, n + 1):

            a, b = b, a + b

        return b


if __name__ == '__main__':
    n=10
    test_back=Back(n)
    print(test_back.backtrack(state=0))

    test_direct=Direct()
    print(test_direct.iteration(i=n))

    test_direct_memory=Direct_Memory(n)
    print(test_direct_memory.iteration_with_memory(i=n))

    test_dp=DP(n)
    print(test_dp.dp(i=n))




