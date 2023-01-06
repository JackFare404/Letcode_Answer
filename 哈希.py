""""""
'''
136. 只出现一次的数字
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

示例 1 ：
输入：nums = [2,2,1]
输出：1
示例 2 ：
输入：nums = [4,1,2,1,2]
输出：4
示例 3 ：
输入：nums = [1]
输出：1
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans


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


def topKFrequent(nums, k: int):
    num = collections.Counter(nums)
    ans = list()
    a = num.most_common(k)
    for i in range(k):
        ans.append((a[i])[0])
    return ans


'''
18. 四数之和
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
'''
def fourSum(nums, target):
    ans = list()
    if not nums or len(nums) < 4:
        return ans
    nums.sort()
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
        #     break
        # if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
        #     break
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
            #     break
            # if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
            #     break
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return ans



