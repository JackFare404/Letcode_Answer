""""""
'''
75. 颜色分类
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1


'''
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 根据快排算法改进的快速选择算法
        res = 0
        def quickselect(nums,k):
            randomIndex = random.randint(0,len(nums)-1)
            pivot = nums[randomIndex]
            left = []
            right = []
            mid = []
            for i in nums:
                if i < pivot:
                    left.append(i)
                elif i > pivot:
                    right.append(i)
                elif i == pivot:
                    mid.append(i)

            if len(right) >= k:
                pivot = quickselect(right,k)

            elif len(right) + len(mid) < k:
                pivot = quickselect(left,k-len(right)-len(mid))

            return pivot
        r = quickselect(nums,k)
        return r

'''
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
'''
import collections
class Solution:
    def topKFrequent(self, nums, k: int):
        num = collections.Counter(nums)
        ans = list()
        a = num.most_common(k)
        for i in range(k):
            ans.append((a[i])[0])
        return ans

'''
451. 根据字符出现频率排序
给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。
返回 已排序的字符串 。如果有多个答案，返回其中任何一个。

示例 1:
输入: s = "tree"
输出: "eert"
解释: 'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:
输入: s = "cccaaa"
输出: "cccaaa"
解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:
输入: s = "Aabb"
输出: "bbAa"
解释: 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        L=sorted(d.keys(),key=lambda x:d[x],reverse=True)
        s=''
        for i in L:
            s+=i*d[i]
        return s
