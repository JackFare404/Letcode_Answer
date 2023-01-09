""""""
'''
88. 合并两个有序数组
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。
示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            if n == 0:
                nums1 = nums1.sort()
            else:
                for i, n in enumerate(nums2):
                    nums1[m+i] = n
                nums1 = nums1.sort()


'''
167. 两数之和 II - 输入有序数组
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
你所设计的解决方案必须只使用常量级的额外空间。

示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total > target:
                high -= 1
            else:
                low += 1

'''
345. 反转字符串中的元音字母
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

示例 1：
输入：s = "hello"
输出："holle"
示例 2：
输入：s = "leetcode"
输出："leotcede"
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        left , right = 0, n - 1
        while left < right:
            while left < n and s[left] not in 'aeiouAEIOU':
                left += 1
            while right > 0 and s[right] not in 'aeiouAEIOU':
                right -= 1
            if left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


'''
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：
输入：c = 3
输出：false
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c)) # int必不可少，否则sum和r会变为小数
        while l <= r:
            sum = l * l + r * r
            if sum == c:
                return True
            elif sum > c:
                r -= 1
            else:
                l += 1
        return False


'''
680. 验证回文串 II
给你一个字符串 s，最多 可以从中删除一个字符。
请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。

示例 1：
输入：s = "aba"
输出：true
示例 2：
输入：s = "abca"
输出：true
解释：你可以删除字符 'c' 。
示例 3：
输入：s = "abc"
输出：false
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, h):
            while l < h:
                if s[l] != s[h]:
                    return False
                else:
                    l += 1
                    h -= 1
            return True

        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(low + 1, high) or check(low, high - 1)
        return True
