import math
# 牛客10道练习题
# https://blog.csdn.net/meiribaofu/article/details/116710453

'''
1、求解连续数列
已知连续正整数数列{K}=K1，K2，K3...Ki的各个数之和为S，i=N(0<S<100000，0<N<100000)，求此数列K。
输入描述：
输入包含两个参数，1）连续正整数数列和S，2）数列里数的个数N。

输出描述：
如果有解输出数列K，如果无解输出-1

示例1：
输入：
525 6
输出：
85 86 87 88 89 90

示例2
输入
3 5
输出
-1
'''
def qiuhe(S, n):
    ans = [0] * n
    middle = int(S / n + 0.5) if n % 2 == 0 else int(S / n)
    start = middle - (n // 2)
    ans[0] = start
    for i in range(1, len(ans)):
        ans[i] = ans[i - 1] + 1
    if ans[0] <= 0:
        return -1
    return ans


print(qiuhe(525, 5))
print(qiuhe(525, 6))
print(qiuhe(3, 3))

'''
2、查找众数及中位数
众数是指一组数据中出现次数量多的那个数，众数可以是多个
中位数是指把一组数据从小到大排列，最中间的那个数，如果这组数据的个数是奇数，那最中间那个就是中位数，如果这组数据的个数为偶数，那就把中间的两个数之和除以2，所得的结果就是中位数
查找整型数组中元素的众数并组成一个新的数组，求新数组的中位数

输入一个一维整型数组，数组大小取值范围
0 < N < 1000，数组中每个元素取值范围
0 < E < 1000

输出描述:
输出众数组成的新数组的中位数

示例1：
输入
10 11 21 19 21 17 21 16 21 18 15
输出
21

示例2：
输入
2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4
输出
3

示例3：
输入
5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39
输出
7
'''
def f(L):
    ans = []
    n = 1
    for i in L:
        if L.count(i) > n:
            ans.clear()
            ans.append(i)
            n = L.count(i)
        if L.count(i) == n:
            if i not in ans:
                ans.append(i)
    ans.sort()
    if len(ans)%2 == 1:
        return int(ans[int((len(ans)-1)/2)])
    else:
        return int((ans[int(len(ans)/2)] + ans[int(len(ans)/2-1)])/2)


print(f([10,11,21,19,21,17,21,16,21,18,15]))
print(f([2,1,5,4,3,3,9,2,7,4,6,2,15,4,2,4]))
print(f([5,1,5,3,5,2,5,5,7,6,7,3,7,11,7,55,7,9,98,9,17,9,15,9,9,1,39]))

'''
3、寻找相同子串
给你两个字符串 t 和 p ，要求从 t 中找到一个和 p 相同的连续子串，并输出该字串第一个字符的下标。

输入描述:
输入文件包括两行，分别表示字符串 t 和 p ，保证 t 的长度不小于 p ，且 t 的长度不超过1000000，p 的长度不超过10000。

输出描述:
如果能从 t 中找到一个和 p 相等的连续子串，则输出该子串第一个字符在t中的下标（下标从左到右依次为1,2,3,…）；如果不能则输出”No”；如果含有多个这样的子串，则输出第一个字符下标最小的。

示例1
输入
AVERDXIVYERDIAN
RDXI
输出
4
'''
def three(t, p):
    if t.count(p) > 0:
        return t.index(p) + 1
    else:
        return 'No'


print(three('AVERDXIVYERDIAN', 'RDXI'))
print(three('AVERDXIVYERDIAN', 'RDdI'))


'''
4、字符串统计
给定两个字符集合，一个为全量字符集，一个为已占用字符集。已占用的字符集中的字符不能再使用，要求输出剩余可用字符集。

输入描述:
1、输入为一个字符串，一定包含@符号。@前的为全量字符集，@后的字为已占用字符集。
2、已占用字符集中的字符一定是全量字符集中的字符。字符集中的字符跟字符之间使用英文逗号分隔。
3、每个字符都表示为字符加数字的形式，用英文冒号分隔，比如a:1，表示1个a字符。
4、字符只考虑英文字母，区分大小写，数字只考虑正整形，数量不超过100。
5、如果一个字符都没被占用，@标识仍然存在，例如a:3,b:5,c:2@

输出描述:
输出可用字符集，不同的输出字符集之间回车换行。
注意，输出的字符顺序要跟输入一致。不能输出b:3,a:2,c:2
如果某个字符已全被占用，不需要再输出。

示例1
输入
a:3,b:5,c:2@a:1,b:2
输出
a:2,b:3,c:2

说明
全量字符集为3个a，5个b，2个c。
已占用字符集为1个a，2个b。
由于已占用字符不能再使用，因此，剩余可用字符为2个a，3个b，2个c。
因此输出a:2,b:3,c:2
'''
def four(s):
    l = s.split('@')
    l1 = l[0].split(',')
    l2 = l[1].split(',')

    d = {}
    for i in l1:
        tmp = i.split(':')
        d[tmp[0]] = int(tmp[1])
    for j in l2:
        tmp = j.split(':')
        d[tmp[0]] = d[tmp[0]] - int(tmp[1])

    ans = ''
    for i in d:
        if d[i] != 0:
            ans = ans + i + ':' + str(d[i]) + ','
    return ans[:-1]


print(four('a:3,b:5,c:2@a:1,b:2'))


'''
5、磁盘容量排序
磁盘的容量单位常用的有M，G，T这三个等级，它们之间的换算关系为1T = 1024G，1G = 1024M，现在给定n块磁盘的容量，请对它们按从小到大的顺序进行稳定排序，例如给定5块盘的容量，1T，20M，3G，10G6T，3M12G9M排序后的结果为20M，3G，3M12G9M，1T，10G6T。注意单位可以重复出现，上述3M12G9M表示的容量即为3M+12G+9M，和12M12G相等。
 
输入描述:
输入第一行包含一个整数n(2 <= n <= 100)，表示磁盘的个数，接下的n行，每行一个字符串(长度大于2，小于30)，表示磁盘的容量，由一个或多个格式为mv的子串组成，其中m表示容量大小，v表示容量单位，例如20M，1T，30G，10G6T，3M12G9M。
磁盘容量m的范围为1到1024的正整数，容量单位v的范围只包含题目中提到的M，G，T三种，换算关系如题目描述。

输出描述:
输出n行，表示n块磁盘容量排序后的结果。

示例1：
输入
3
1G
2G
1024M
输出
1G
1024M
2G

说明
1G和1024M容量相等，稳定排序要求保留它们原来的相对位置，故1G在1024M之前

示例2：
输入
3
2G4M
3M2G
1T
输出
3M2G
2G4M
1T

说明
1T的容量大于2G4M，2G4M的容量大于3M2G
'''
import re

def five(n, s):
    S = s.split()
    res = []
    ans = []
    for i in S:
        A = re.findall("\d+\w", i)
        # A = []
        # A.append(i)
        size = 0
        for a in A:
            if a[-1] == "M":
                size += int(a[:-1])
            elif a[-1] == "G":
                size += int(a[:-1])*1024
            elif a[-1] == "T":
                size += int(a[:-1])*1024*1024
            else:
                size += int(a)
        res.append((i, size))
    L = sorted(res, key=lambda x: x[1])
    # def paixu(x):
    #     return x[1]
    # res.sort(key=paixu)
    # L = res
    for j in L:
        ans.append(j[0])
    return ans


print(five(3, '1G 2G 1024M'))
print(five(3, '2G4M 3M2G 1T'))


'''
6、太阳能板最大面积
给航天器一侧加装长方形或正方形的太阳能板（图中的红色斜线区域），需要先安装两个支柱（图中的黑色竖条），再在支柱的中间部分固定太阳能板。但航天器不同位置的支柱长度不同，太阳能板的安装面积受限于最短一侧的那根支柱长度。如图：
现提供一组整形数组的支柱高度数据，假设每根支柱间距离相等为1个单位长度，计算如何选择两根支柱可以使太阳能板的面积最大。

输入描述:
10,9,8,7,6,5,4,3,2,1
注：支柱至少有2根，最多10000根，能支持的高度范围1~10^9的整数。柱子的高度是无序的，例子中递减只是巧合。

输出描述:
可以支持的最大太阳能板面积：（10米高支柱和5米高支柱之间）
25

示例1
输入
10,9,8,7,6,5,4,3,2,1
输出
25
备注:
10米高支柱和5米高支柱之间宽度为5，高度取小的支柱高也是5，面积为25。任取其他两根支柱所能获得的面积都小于25。所以最大的太阳能板面积为25。
'''
def six(n):
    nums = list(map(int, n.split(",")))
    max_area = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            temp_area = min(nums[i:j + 1]) * (j - i)
            if temp_area > max_area:
                max_area = temp_area
    return max_area


print(six('10,9,8,7,6,5,4,3,2,1'))


'''
7、靠谱的车
程序员小明打了一辆出租车去上班。出于职业敏感，他注意到这辆出租车的计费表有点问题，总是偏大。
出租车司机解释说他不喜欢数字4，所以改装了计费表，任何数字位置遇到数字4就直接跳过，其余功能都正常。

比如：
1.23再多一块钱就变为25；
2.39再多一块钱变为50；
3.399再多一块钱变为500；
小明识破了司机的伎俩，准备利用自己的学识打败司机的阴谋。
给出计费表的表面读数，返回实际产生的费用。

输入描述:
只有一行，数字N，表示里程表的读数。
(1<=N<=888888888)。
输出描述:
一个数字，表示实际产生的费用。以回车结束。

示例1：
输入
5
输出
4
说明
5表示计费表的表面读数。
4表示实际产生的费用其实只有4块钱。

示例2：
输入
17
输出
15
说明
17表示计费表的表面读数。
15表示实际产生的费用其实只有15块钱。

示例3：
输入
100
输出
81
说明
100表示计费表的表面读数。
81表示实际产生的费用其实只有81块钱。
'''
def seven(n):
    chajia = 0
    for i in range(n):
        if '4' in str(i):
            chajia = chajia + 1
    ans = n - chajia
    return ans


print(seven(5))
print(seven(17))
print(seven(100))


'''
8、整数对最小和
给定两个整数数组array1、array2，数组元素按升序排列。假设从array1、array2中分别取出一个元素可构成一对元素，现在需要取出k对元素，并对取出的所有元素求和，计算和的最小值
注意：两对元素如果对应于array1、array2中的两个下标均相同，则视为同一对元素。

输入描述:
输入两行数组array1、array2，每行首个数字为数组大小size(0 < size <= 100);
0 < array1[i] <= 1000
0 < array2[i] <= 1000
接下来一行为正整数k
0 < k <= array1.size() * array2.size()
输出描述:
满足要求的最小和
 
示例1
输入
3 1 1 2
3 1 2 3
2
输出
4

说明
用例中，需要取2对元素
取第一个数组第0个元素与第二个数组第0个元素组成1对元素[1,1];
取第一个数组第1个元素与第二个数组第0个元素组成1对元素[1,1];
求和为1+1+1+1=4，为满足要求的最小和
'''
def eight(arr1, arr2, k):
    arr1 = list(map(int, arr1.split()))
    arr2 = list(map(int, arr2.split()))
    list1 = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            list1.append(arr1[i]+arr2[j])
    ans = 0
    list1.sort()
    for i in range(k):
        ans += list1[i]
    return ans


print(eight('3 1 1 2', '3 1 2 3', 2))

'''
9、判断字符串子序列
给定字符串 target和 source, 判断 target 是否为 source 的子序列。
你可以认为 target 和  source 中仅包含英文小写字母。字符串 source可能会很长（长度 ~= 500,000），而 target 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"abc"是"aebycd"的一个子序列，而"ayb"不是）。
请找出最后一个子序列的起始位置。

输入描述:
第一行为target，短字符串（长度 <=100）
第二行为source，长字符串（长度 ~= 500,000）

输出描述:
最后一个子序列的起始位置， 即最后一个子序列首字母的下标
示例1
输入
abc
abcaybec
输出
3

说明
这里有两个abc的子序列满足，取下标较大的，故返回3
备注:
若在source中找不到target，则输出-1
'''
def nine(target, source):
    i = len(target) - 1
    j = len(source) - 1
    index = 0
    while i >= 0:
        index = 0
        while j >= 0:
            if target[i] == source[j]:
                index = j
                j -= 1
                break
            else:
                index = j
                j -= 1
                continue
        i -= 1
    return index


print(nine('abc', 'abcaybec'))


'''
10、按身高和体重排队
某学校举行运动会，学生们按编号(1、2、3…n)进行标识，现需要按照身高由低到高排列，对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。
输入描述:
两个序列，每个序列由n个正整数组成（0 < n <= 100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。
输出描述:
排列结果，每个数值都是原始序列中的学生编号，编号从1开始

示例1：
输入
4
100 100 120 130
40 30 60 50
输出
2 1 3 4
说明
输出的第一个数字2表示此人原始编号为2，即身高为100，体重为30的这个人。由于他和编号为1的人身高一样，但体重更轻，因此要排在1前面。

示例2：
输入
3
90 110 90
45 60 45
输出
1 3 2
说明
1和3的身高体重都相同，需要按照原有位置关系让1排在3前面，而不是3 1 2
'''
def ten(n, height, weight):
    h = list(map(int, height.split()))
    w = list(map(int, weight.split()))
    n = int(n)
    res = []
    ans = []
    for i in range(1, n+1):
        res.append((i, h[i-1], w[i-1]))

    # def paixu(x):
    #     return x[1], x[2]
    # res.sort(key=paixu)
    res = sorted(res, key=lambda x: (x[1], x[2]))

    return ' '.join([str(j[0]) for j in res])
    # for j in res:
    #     ans.append(str(j[0]))
    # ans = ' '.join(ans)
    # return ans


print(ten('4', '100 100 120 130', '40 30 60 50'))
print(ten('3', '90 110 90', '45 60 45'))
