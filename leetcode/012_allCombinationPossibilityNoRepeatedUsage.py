# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。

class Combination2(object):
    def __init__(self,nums:list,target:int):
        self.nums_sort=sorted(nums)
        self.target=target
        self.ans=[]
        self.res=[]
        self.n=len(nums)

    def backtrack(self,i):
        # 停止条件
        if sum(self.ans) == self.target and self.ans not in self.res:
            self.res.append(self.ans[:])
            return

        if sum(self.ans) > self.target:
            return

        # 回溯部分
        for t in range(i,self.n):
            # 操作
            self.ans.append(self.nums_sort[t])

            self.backtrack(t+1)

            self.ans.pop()

        return self.res


if __name__ == '__main__':
    nums=[10,1,2,7,6,1,5]
    target=8
    test=Combination2(nums=nums,target=target)
    print(test.backtrack(0))