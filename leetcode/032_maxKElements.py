# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。你的 起始分数 为 0 。
#
# 在一步 操作 中：
#
# 选出一个满足 0 <= i < nums.length 的下标 i ，
# 将你的 分数 增加 nums[i] ，并且
# 将 nums[i] 替换为 ceil(nums[i] / 3) 。
# 返回在 恰好 执行 k 次操作后，你可能获得的最大分数。
#
# 向上取整函数 ceil(val) 的结果是大于或等于 val 的最小整数。


# 输入：nums = [1,10,3,3,3], k = 3
# 输出：17
# 解释：可以执行下述操作：
# 第 1 步操作：选中 i = 1 ，nums 变为 [1,4,3,3,3] 。分数增加 10 。
# 第 2 步操作：选中 i = 1 ，nums 变为 [1,2,3,3,3] 。分数增加 4 。
# 第 3 步操作：选中 i = 2 ，nums 变为 [1,1,1,3,3] 。分数增加 3 。
# 最后分数是 10 + 4 + 3 = 17 。

from math import ceil
from heapq import heapify,heapreplace


def maxKElements(nums:list[int],k:int)->int:

    for i in range(len(nums)):
        nums[i] = -nums[i]  # 最大堆
    heapify(nums)  # 原地堆化
    ans = 0
    for _ in range(k):
        ans -= heapreplace(nums, nums[0] // 3)
    return ans



if __name__ == '__main__':
    nums=[10,10,10,10,10]
    k = 5
    print(maxKElements(nums,k))