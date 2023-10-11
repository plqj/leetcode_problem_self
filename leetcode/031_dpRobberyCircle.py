# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

# 思路：分类讨论第一家偷不偷，然后在不同区间上做之前的030的dp，取大的那个

def dpRobberyCircle(nums):
    def sub(start,end):
        prev = 0
        curr = 0
        for i in nums[start:end]:
            # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            prev, curr = curr, max(curr, prev + i)
            # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
        return curr

    length = len(nums)
    if length == 1:
        return nums[0]
    elif length == 2:
        return max(nums[0], nums[1])
    else:
        return max(sub(0, length - 1), sub(1, length))


if __name__ == '__main__':
    nums=[6,3,6]
    print(dpRobberyCircle(nums))