# 给定一个可包含重复数字的序列nums ，按任意顺序返回所有不重复的全排列。

class Permutation2(object):
    def __init__(self,nums):
        self.nums=nums
        self.res=[]
        self.n=len(nums)
        self.used=[False]*self.n
        self.ans=[]

    def backtrack(self,i):
        if i == self.n and self.ans not in self.res:
            self.res.append(self.ans[:])
            return

        for t in range(self.n):
            if self.used[t]:
                continue

            # 前进
            self.ans.append(self.nums[t])
            self.used[t] = True

            # 递归
            self.backtrack(i + 1)

            # 回溯
            self.ans.pop()
            self.used[t] = False

        return len(self.res), self.res


if __name__ == '__main__':
    nums=[1,2,1]
    test=Permutation2(nums)
    print(test.backtrack(0))