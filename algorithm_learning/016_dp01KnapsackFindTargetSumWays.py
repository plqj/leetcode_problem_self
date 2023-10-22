# 给你一个非负整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

from functools import cache


def findTargetSumWays(nums: list[int], target: int) -> int:
    target += sum(nums)
    if target < 0 or target % 2:
        return 0
    target //= 2

    @cache  # 记忆化搜索
    def dfs(i, c):
        if i < 0:
            return 1 if c == 0 else 0
        if c < nums[i]:
            return dfs(i - 1, c)
        return dfs(i - 1, c) + dfs(i - 1, c - nums[i])

    return dfs(len(nums) - 1, target)



if __name__ == '__main__':
    nums=[1,1,1,1,1]
    target = 3
    print(findTargetSumWays(nums,target))