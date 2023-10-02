# 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。

class Permutation(object):
    def __init__(self,nums):
        self.nums=nums
        self.res=[]
        self.n=len(nums)
        self.used=[False]*self.n
        self.ans=[]

    def backtrack(self,i):
        if i == self.n:
            self.res.append(self.ans[:])
            return

        for t in range(self.n):
            # 判断是否用过了
            if self.used[t]:
                continue

            # 前进
            self.ans.append(self.nums[t])
            self.used[t]=True

            # 递归
            self.backtrack(i+1)

            # 回溯
            self.ans.pop()
            self.used[t]=False

        return len(self.res),self.res


if __name__ == '__main__':
    nums=[1,2,3,4]
    test=Permutation(nums)
    print(test.backtrack(0))