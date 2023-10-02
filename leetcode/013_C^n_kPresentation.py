# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。

# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class C_nk(object):
    def __init__(self,n,k):
        self.n=n
        self.k=k
        self.candidates=[i for i in range(1,self.n+1)]
        self.res=[]
        self.ans=[]


    def backtrack(self,i):
        if len(self.ans) == self.k:
            self.res.append(self.ans[:])
            return

        for t in range(i,self.n-(self.k-len(self.ans))+1):

            self.ans.append(self.candidates[t])

            self.backtrack(t+1) # 哪个是会改变的？是t，所以这里迭代时进入的是t

            self.ans.pop()

        return self.res



if __name__ == '__main__':
    n=4
    k=2
    test=C_nk(n=n,k=k)
    print(test.backtrack(0))