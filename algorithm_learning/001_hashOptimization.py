# 给定一个整数数组 nums 和一个目标元素 target
# 请在数组中搜索“和”为target的两个元素，并返回它们的数组索引。返回任意一个解即可。

# 实验结果：哪怕在小规模上，hash search也用时更短，体现了哈希查找的时间优越性。

import time

class Algorithms(object):
    def __init__(self,nums:list,target:int):
        self.nums=nums
        self.target=target
        self.length=len(nums)

    def linear_search(self):
        """
        gain spatial advantage at the cost of time. Directly search all possible pair and calculate if they satisfy.
        Space: O(1)
        Time: O(n^2)
        :return: the first possible pair, else False
        """
        for i in range(self.length-1):
            for j in range(i+1,self.length):
                if self.nums[i]+self.nums[j]==self.target:
                    return (i,j)
        return False

    def hash_search(self):
        """
        With the help of an assisting Dictionary time is saved
        Space: O(n)
        Time: O(n)
        :return: the first possible pair, else False
        """
        # Assisting hash table
        dic = {}

        for i in range(self.length):
            if self.target - self.nums[i] in dic:
                return [dic[self.target - self.nums[i]], i]
            dic[self.nums[i]] = i
        return False

    def main(self):
        print(f"start linear search timing...")
        t1=time.time()
        print(self.linear_search())
        t2=time.time()
        print(f"linear search costs {t2-t1}")

        print(f"start hash search timing...")
        t3=time.time()
        print(self.hash_search())
        t4=time.time()
        print(f"hash search costs {t4-t3}")


if __name__ == '__main__':
    nums=[2,4,6,7,3,5,7,8,2,4,6,3,7,4,7,9,3,6,2,5,4,10,2,345,63,2,45,1,45,1,3,6,2,34,5,23,4,6,242,5,63,5,2,34]
    target=587
    test=Algorithms(nums=nums,target=target)
    test.main()


