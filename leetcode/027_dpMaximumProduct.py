# 给你一个整数数组 nums
# 请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
# 子数组 是数组的连续子序列。

# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。


# def dpMaximumProduct(nums:list[int]) -> int:
#     n=len(nums)
#
#     if n==1:
#         return nums[0]
#
#     dp=[0 for _ in range(n)]
#     dp[0]=nums[0]
#
#     for i in range(1,n):
#         dp[i]=max(dp[i-1]*nums[i],nums[i])
#
#     return max(dp)

def maxProduct(nums: list[int]) -> int:
    reverse_nums = nums[::-1]
    for i in range(1, len(nums)):
        nums[i] *= nums[i - 1] or 1 # 如果nums[i]为零，则nums[i]的值为1
        reverse_nums[i] *= reverse_nums[i - 1] or 1
    return max(nums + reverse_nums)



if __name__ == '__main__':
    nums= [2,3,-2,4,7,-5]
    # print(dpMaximumProduct(nums))
    print(maxProduct(nums))