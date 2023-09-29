# 实现在O(nlogn)快速排序

class QuickSort(object):
    def __init__(self,nums):
        self.nums=nums
        self.length=len(nums)

    def quick_sort(self,l:list):
        if len(l) <= 1:
            return l

        pivot = l[len(l) // 2]
        left = []
        right = []
        equal = []

        for element in l:
            if element < pivot:
                left.append(element)
            elif element > pivot:
                right.append(element)
            else:
                equal.append(element)

        return self.quick_sort(left) + equal + self.quick_sort(right)




if __name__ == '__main__':
    nums = [3, 6, 8, 10, 1, 2, 1,3,5,7,2,4,8,13,7]
    test=QuickSort(nums)
    sorted_list = test.quick_sort(nums)
    print(sorted_list)
