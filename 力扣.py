""""""
'''
1047. 删除字符串中的所有相邻重复项————牛客2-10消消乐
给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
S 仅由小写英文字母组成。
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ls = []
        for i in s:
            if ls and i == ls[-1]:
                ls.pop()
            else:
                ls.append(i)
        return ''.join(ls)


'''
392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

示例 1：
输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：
输入：s = "axc", t = "ahbgdc"
输出：false

两个字符串都只由小写字符组成。
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n


'''
179. 最大数————牛客2-5
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"
示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"
'''
def five(num):
    # num = num.split(',')
    # for n in range(len(num)):
    #     num[n] = int(num[n])

    for i in range(len(num)):
        for j in range(0, len(num)-1):
            if str(num[j]) + str(num[j+1]) < str(num[j+1]) + str(num[j]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    ans = ''
    for a in range(len(num)):
        ans = ans + str(num[a])
    if ans[0] == '0':
        ans = '0'
    return ans

print(five([10,2]))
print(five([3,30,34,5,9]))


'''
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
示例 1：
输入：m = 3, n = 7
输出：28
示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：
输入：m = 7, n = 3
输出：28
示例 4：
输入：m = 3, n = 3
输出：6
'''
def uniquePaths(m: int, n: int) -> int:
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


'''
3. 无重复字符的最长子串  哈希/字符串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


def lengthOfLongestSubstring(s: str) -> int:  # 注意类的self
    cur = []
    ans = 0
    for i in range(len(s)):
        while s[i] in cur:
            cur.pop(0)
        cur.append(s[i])
        ans = max(ans, len(cur))
    return ans


'''
1593. 拆分字符串使唯一子字符串的数目最大
给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。
字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。
注意：子字符串 是字符串中的一个连续字符序列。

示例 1：
输入：s = "ababccc"
输出：5
解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
示例 2：
输入：s = "aba"
输出：2
解释：一种最大拆分方法为 ['a', 'ba'] 。
示例 3：
输入：s = "aa"
输出：1
解释：无法进一步拆分字符串。
'''


def maxUniqueSplit(s: str) -> int:
    def traceback(index, split):
        if index >= n:
            nonlocal maxsplit
            maxsplit = max(maxsplit, split)
        else:
            for i in range(index, n):
                substr = s[index:i+1]
                if substr not in cur:
                    cur.append(substr)
                    traceback(i + 1, split + 1)
                    cur.remove(substr)
    n = len(s)
    cur = []
    maxsplit = 1
    traceback(0, 0)
    return maxsplit


'''
剑指 Offer 13面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3
示例 2：
输入：m = 3, n = 1, k = 0
输出：1
'''


def movingCount(m: int, n: int, k: int) -> int:
    def dfs(i, j, si, sj):
        if i >= m or j >= n or k < si + sj or (i, j) in visited:
            return 0
        visited.add((i, j))
        return \
            1 + \
            dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
            dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

    visited = set()
    return dfs(0, 0, 0, 0)


'''
1371. 每个元音包含偶数次的最长子字符串
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

示例 1：
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：
输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
'''


def findTheLongestSubstring(s: str) -> int:
    dict = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}  # 这个提前打好，避免主循环里冗长的if-else
    seen = {0: -1}  # 一定要预先加入0状态，否则会漏掉从s[0]开始的子串
    cur, ans = 0, 0
    for idx, word in enumerate(s):
        if word in dict:
            cur ^= dict[word]  # 用异或操作来给当前字母对应的位取反
        if cur in seen:  # 见过的状态，更新答案即可，不要画蛇添足用j把seen[cur]顶掉，我们要的是最长子串
            ans = max(ans, idx - seen[cur])
        else:  # 没见过的状态放入哈希表
            seen[cur] = idx
    return ans
