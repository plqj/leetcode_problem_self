# 堆排序的从零实现

def heapify(arr, n, i):
    """
    :param arr: heap to be heapified
    :param n: length of the heap
    :param i: father node under check
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 找到左子节点和右子节点中的较大值
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点，则交换它们，并递归地调整子树
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 构建最大堆,假设长度为n，则最后一个拥有哪怕只有一个左子堆的父节点编号为n//2-1, 所以直接从n//2-1这个编号开始逆序搜索至0即可
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 逐个提取元素并排序
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换根节点和最后一个节点
        heapify(arr, i, 0)  # 重新调整最大堆

# 示例用法
arr = [7,2,3,1,5,6,2,4,8 ]
heap_sort(arr)
print(arr)