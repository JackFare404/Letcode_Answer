# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 方法一：常规思想
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        lens = m + n
        old, new = -1, -1
        Astart, Bstart = 0, 0
        for i in range(lens // 2 + 1):
            old = new   # 每次循环前将 new 的值赋给 old
            if Astart < m and (Bstart >= n or A[Astart] < B[Bstart]):    # A移动的条件: B遍历到最后 或 当前A<B,满足一个即可
                new = A[Astart]
                Astart += 1
            else:
                new = B[Bstart]
                Bstart += 1
        if (lens & 1) == 0:   # 与1交,判断奇偶数,更快速
            return (old + new) / 2.0
        else:
            return new





# 方法二：第k小数
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        def getKthElement(k):
            idx1, idx2 = 0, 0
            while True: # 特殊情况
                if idx1 == m:
                    return B[idx2 + k - 1]
                if idx2 == n:
                    return A[idx1 + k - 1]
                if k == 1:
                    return min(A[index1], B[index2])

                # 正常情况,index1,index2作为起始点,newindex1,newindex2作为比较点 在不停的更新
                newidx1 = min(idx1 + k // 2 - 1, m - 1) # 第一种特殊情况,发生越界,记录需要比较的位置
                newidx2 = min(idx2 + k // 2 - 1, n - 1) # 第二种特殊情况,发生越界,记录需要比较的位置
                pivot1, pivot2 = A[newidx1], B[newidx2] # 获取两个需要比较的数
                if pivot1 <= pivot2: # <=将两种情况合并
                    k -= newidx1 - idx1 + 1 # 两者相减后+1,这才是真正减去的长度
                    idx1 = newidx1 + 1  # 连同比较位置也一同删去了,所以新的开始是 比较位置 的后一位
                else:
                    k -= newidx2 - idx2 + 1
                    idx2 = newidx2 + 1

        m, n = len(A), len(B)
        lens = m + n
        if lens % 2 == 1:   # 可以将两种情况合并,奇数会求两次同样的k
            return getKthElement((lens + 1) // 2)
        else:
            return (getKthElement(lens // 2) + getKthElement(lens // 2 + 1)) / 2

# 方法三：划分数组
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)

        infinty = 2 ** 40   # 代表正无穷
        m, n = len(A), len(B)
        left, right = 0, m
        median1, median2 = 0, 0
        # median1：前一部分的最大值
        # median2：后一部分的最小值

        while left <= right:    # 一直循环找到一个最大的i满足A[i−1]≤B[j]
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            # 当一个数组不出现在前一部分时,对应的值为负无穷,就不会对前一部分的最大值产生影响
            A_im1 = (-infinty if i == 0 else A[i - 1])  # 注意写法与java不同
            # 当一个数组不出现在后一部分时,对应的值为正无穷,就不会对后一部分的最小值产生影响
            A_i = (infinty if i == m else A[i])
            B_jm1 = (-infinty if j == 0 else B[j - 1])
            B_j = (infinty if j == n else B[j])

            if A_im1 <= B_j:
                median1, median2 = max(A_im1, B_jm1), min(A_i, B_j)
                left = i + 1
            else:
                right = i - 1

        if (m + n) % 2 == 1:
            return median1
        else:
            return (median1 + median2) / 2




# if __name__ == '__main__':
#     T = Solution()
#     print(T.)
