# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。
# 换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
#
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。


def jump(nums:list[int]):
        size = len(nums)
        dp = [float("inf") for _ in range(size)]
        dp[0] = 0

        for i in range(1, size):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[size - 1]



if __name__ == '__main__':
    nums = [2, 3, 1,1, 4,1,3,6,2,5,7,3,6,1,2,3,2,1,2,1]
    print(jump(nums))