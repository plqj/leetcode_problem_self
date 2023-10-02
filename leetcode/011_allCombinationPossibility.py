# 给你一个无重复元素的整数数组 candidates 和一个目标整数 target
# 找出 candidates 中可以使数字和为目标数 target 的所有不同组合
# 并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的 同一个 数字可以 无限制重复被选取
# 如果至少一个数字的被选数量不同，则两种组合是不同的。

# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。

# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]

class Combination(object):
    def __init__(self,nums:list,target:int):
        self.nums=nums
        self.target=target
        self.res=[]
        self.ans=[]
        self.n=len(nums)

    def backtrack(self,i):
        # 停止条件
        if sum(self.ans) == self.target:
            self.res.append(self.ans[:])
            return

        if sum(self.ans)>self.target: # 提前判断“和”超过了就行，不用把整个数组都遍历完
            return

        for t in range(i,self.n):
            # 前进
            self.ans.append(self.nums[t])

            self.backtrack(t) # 从当前这个数字开始找就行，这样前面已经pass掉的就不会重复拿来用了

            self.ans.pop()

        return self.res


if __name__ == '__main__':
    nums=[2,3,6,7,1,4]
    target=7
    test=Combination(nums=nums,target=target)
    print(test.backtrack(0))
