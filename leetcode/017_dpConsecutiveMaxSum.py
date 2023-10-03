# 给定一个整数数组，找出总和最大的连续数列，并返回总和。
#
# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。


def maxSubArray(nums):
    cnt, ret = 0, nums[0]
    for num in nums:
        cnt = max(num, cnt + num)
        ret = max(ret, cnt)
    return ret


if __name__ == '__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))