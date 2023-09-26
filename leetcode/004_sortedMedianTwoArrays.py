# 给定两个大小分别为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数 。算法的时间复杂度应该为O(log(m + n)) 。
#
# 示例
# 1：
#
# 输入：nums1 = [1, 3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1, 2, 3] ，中位数
# 2
# 示例
# 2：
#
# 输入：nums1 = [1, 2], nums2 = [3, 4]
# 输出：2.50000
# 解释：合并数组 = [1, 2, 3, 4] ，中位数(2 + 3) / 2 = 2.5

class Median_Search(object):
    def __init__(self,nums1,nums2):
        self.nums1=nums1 # 第一个数组
        self.nums2=nums2 # 第二个数组
        self.m=len(nums1) # 第一数组长度
        self.n=len(nums2) # 第二数组长度


    def main(self):
        left, right = 0, self.m
        half = (self.m + self.n + 1) // 2
        while left < right:
            i = (left + right) // 2
            j = half - i
            if self.nums1[i] < self.nums2[j - 1]:
                left = i + 1
            else:
                right = i
        i, j = left, half - left

        if i == 0:
            mid1 = self.nums2[j - 1]
        elif j == 0:
            mid1 = self.nums1[i - 1]
        else:
            mid1 = max(self.nums1[i - 1], self.nums2[j - 1])
        if (self.m + self.n) & 1:
            return mid1

        if i == self.m:
            mid2 = self.nums2[j]
        elif j == self.n:
            mid2 = self.nums1[i]
        else:
            mid2 = min(self.nums1[i], self.nums2[j])
        return (mid1 + mid2) / 2



if __name__ == "__main__":
    nums1=[1,2,4]
    nums2=[1,2,5,7,9]
    test=Median_Search(nums1,nums2)
    print(test.main())