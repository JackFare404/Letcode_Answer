# 牛客10道练习题2
# https://blog.csdn.net/meiribaofu/article/details/116710453

"""
1、快递运输  数组
一辆运送快递的货车，运送的快递均放在大小不等的长方体快递盒中，为了能够装载更多的快递，同时不能让货车超载，需要计算最多能装多少个快递。
注：快递的体积不受限制，快递数最多1000个，货车载重最大50000。

输入描述:
第一行输入每个快递的重量，用英文逗号分隔，如：5,10,2,11
第二行输入货车的载重量，如：20
不需要考虑异常输入。
输出描述:
输出最多能装多少个快递，如：3

示例1：
输入
5,10,2,11
20
输出
3
说明
货车的载重量为20，最多只能放三个快递5、10、2，因此输出3
"""


def one(weight, number):
    w = list(map(int, weight.split(',')))
    n = int(number)

    w.sort()
    sums = 0
    count = 0
    for i in w:
        if sums + i <= n:
            sums += i
            count += 1
        else:
            break
    return count


print(one('5,10,2,11', '20'))

'''
2、TLV解码 数组
TLV编码是按[Tag Length Value]格式进行编码的，一段码流中的信元用Tag标识，Tag在码流中唯一不重复，Length表示信元Value的长度，Value表示信元的值。
码流以某信元的Tag开头，Tag固定占一个字节，Length固定占两个字节，字节序为小端序。
# 大端序（Big-Endian）将数据的低位字节存放在内存的高位地址，高位字节存放在低位地址。这种排列方式与数据用字节表示时的书写顺序一致，符合人类的阅读习惯。
# 小端序（Little-Endian），将一个多位数的低位放在较小的地址处，高位放在较大的地址处，则称小端序。
现给定TLV格式编码的码流，以及需要解码的信元Tag，请输出该信元的Value。
输入码流的16机制字符中，不包括小写字母，且要求输出的16进制字符串中也不要包含小写字母；码流字符串的最大长度不超过50000个字节。

输入描述:
输入的第一行为一个字符串，表示待解码信元的Tag；
输入的第二行为一个字符串，表示待解码的16进制码流，字节之间用空格分隔。
输出描述:
输出一个字符串，表示待解码信元以16进制表示的Value。

示例1：
输入
31
32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
输出
32 33

说明
需要解析的信元的Tag是31，从码流的起始处开始匹配，Tag为32的信元长度为1（01 00，小端序表示为1）；第二个信元的Tag是90，其长度为2；第三个信元的Tag是30，其长度为3；第四个信元的Tag是31，其长度为2（02 00），所以返回长度后面的两个字节即可，即32 33。
'''
def two(tag1, tlv):
    tlv = tlv.split()
    i = 0

    while i < len(tlv):
        tag = tlv[i]
        length = int(tlv[i + 2] + tlv[i + 1], 16)
        value = ''
        for j in range(length):
            value += tlv[i + 3 + j] + ' '
        i = i + 3 + length
        if tag1 == tag:
            return value


print(two('31', '32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC'))

'''
3、考勤信息  字符串
公司用一个字符串来表示员工的出勤信息：
absent：缺勤
late：迟到
leaveearly：早退
present：正常上班
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：
缺勤不超过一次；没有连续的迟到/早退；任意连续7次考勤，缺勤/迟到/早退不超过3次

输入描述:
用户的考勤数据字符串，记录条数 >= 1；输入字符串长度<10000；不存在非法输入
如：
2
present
present absent present present leaveearly present absent
输出描述:
根据考勤数据字符串，如果能得到考勤奖，输出"true"；否则输出"false"，对于输入示例的结果应为：
true false

示例1：
输入
2
present
present present
输出
true true

示例2：
输入
2
present
present absent present present leaveearly present absent
输出
true false
'''
def three(num, record):
    num = int(num)
    ans = []
    for i in range(num):
        if record[i].count('absent') > 1:
        # if 'absent' in record[i]:
            ans.append('false')
            continue
        if record[i].count('late late') or record[i].count('leaveearly leaveearly') or record[i].count('late leaveearly') or record[i].count('leaveearly late'):
            ans.append('false')
            continue
        record1 = record[i].split()
        for j in range(len(record1)):
            if record1[j] == 'absent' or record1[j] == 'late' or record1[j] == 'leaveearly':
                nums = 0
                l = record1[j+1:j+7]
                nums += l.count('absent')
                nums += l.count('late')
                nums += l.count('leaveearly')
                if nums > 2:
                    ans.append('false')
                    continue
        ans.append('true')
    return ans


print(three('3', ['absent present present present present present present present present late late',
                  'absent present present present late present present leaveearly present present present late present present',
                  'absent present late present present present present late leaveearly present present']))
print(three('2', ['absent leaveearly present late present', 'present absent present present present present']))
print(three('1', ['present leaveearly present late present present absent present present present present']))
print(three('2', ['present', 'present present']))
print(three('2', ['present', 'leaveearly late present present']))

'''
4、字符串分割 字符串
给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。
对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；
反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。

输入描述:
输入为两行，第一行为参数K，第二行为字符串S。
输出描述:
输出转换后的字符串。

示例1
输入
3
12abc-abCABc-4aB@
输出
12abc-abc-ABC-4aB-@
说明
子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每3个字符一组为abC、ABc、4aB、@，abC中小写字母较多，转换为abc，ABc中大写字母较多，
转换为ABC，4aB中大小写字母都为1个，不做转换，@中没有字母，连起来即12abc-abc-ABC-4aB-@

示例2

输入
12
12abc-abCABc-4aB@
输出
12abc-abCABc4aB@

说明
子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每12个字符一组为abCABc4aB@，这个子串中大小写字母都为4个，不做转换，连起来即12abc-abCABc4aB@
'''
def four(k, string):
    head, tail = string.split('-', 1)
    tail = tail.replace('-', '')
    temp = ''
    for i in range(0, len(tail), k):
        line = tail[i:i+k]
        count1 = 0
        count2 = 0
        for c in line:
            if 'A'<= c <='Z':
                count1 += 1
            if 'a'<= c <='z':
                count2 += 1
        if count1 == count2:
            temp += line
        elif count1 > count2:
            temp += line.upper()
        else:
            temp += line.lower()
    ans = []
    for j in range(0, len(temp), k):
        ans.append(temp[j:j+k])
    ans = head + '-' + '-'.join(ans)
    return ans
    # return f"{head}-{'-'.join(ans)}"


print(four(3, '12abc-abCABc-4aB@'))
print(four(12, '12abc-abCABc-4aB@'))

'''
5、组成最大数 排序
小组中每位都有一张卡片，卡片上是6位内的正整数，将卡片连起来可以组成多种数字，计算组成的最大数字。

输入描述:
“,”号分割的多个正整数字符串，不需要考虑非数字异常情况，小组最多25个人
输出描述:
最大的数字字符串

示例1
输入
22,221
输出
22221

示例2
输入
4589,101,41425,9999
输出
9999458941425101
'''

def five(num):
    num = num.split(',')
    for n in range(len(num)):
        num[n] = int(num[n])

    for i in range(len(num)):
        for j in range(0, len(num)-1):
            if str(num[j]) + str(num[j+1]) < str(num[j+1]) + str(num[j]):
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    ans = ''
    for a in range(len(num)):
        ans = ans + str(num[a])
    return ans

print(five('22,221'))
print(five('4589,101,41425,9999'))


'''
6、高矮个子排队    排序
现在有一队小朋友，他们高矮不同，我们以正整数数组表示这一队小朋友的身高，如数组{5,3,1,2,3}。
我们现在希望小朋友排队，以“高”“矮”“高”“矮”顺序排列，每一个“高”位置的小朋友要比相邻的位置高或者相等；每一个“矮”位置的小朋友要比相邻的位置矮或者相等；
要求小朋友们移动的距离和最小，第一个从“高”位开始排，输出最小移动距离即可。
例如，在示范小队{5,3,1,2,3}中，{5, 1, 3, 2, 3}是排序结果。{5, 2, 3, 1, 3} 虽然也满足“高”“矮”“高”“矮”顺序排列，但小朋友们的移动距离大，所以不是最优结果。
移动距离的定义如下所示：
第二位小朋友移到第三位小朋友后面，移动距离为1，若移动到第四位小朋友后面，移动距离为2；

输入描述:
排序前的小朋友，以英文空格的正整数：
4 3 5 7 8
注：小朋友<100个
输出描述:
排序后的小朋友，以英文空格分割的正整数：
4 3 7 5 8

示例1：
输入
4 1 3 5 2
输出
4 1 5 2 3

示例2：
输入
1 1 1 1 1
输出
1 1 1 1 1
说明
相邻位置可以相等
示例3：
输入
xxx
输出
[ ]
说明：
出现非法参数情况， 返回空数组
备注:
4（高）3（矮）7（高）5（矮）8（高）， 输出结果为最小移动距离，只有5和7交换了位置，移动距离都是1。
'''
def six(child):
    try:
        child = list(map(int,child.split()))
        child1 = child.copy()
        child1.sort(reverse=True)

        if len(child1)%2==0:
            e = len(child1) // 2
        else:
            e = len(child1) // 2 + 1

        for i in range(0, len(child), 2):
            if child[i] not in child1[0:e]:
                for j in range(1, len(child), 2):
                    if child[j] in child1[0:e]:
                        temp = child[i]
                        child[i] = child[j]
                        child[j] = temp
                        break
        ans = ' '.join(map(str, child))
        return ans

    except Exception as e:
        return "[]"


print(six('4 1 3 5 2'))
print(six('1 1 1 1 1'))
print(six('xxx'))
print(six('4 3 5 7 8'))
print(six('10 8 6 9 9'))

'''
7、猴子爬山    递归
一天一只顽猴想去从山脚爬到山顶，途中经过一个有个N个台阶的阶梯，但是这猴子有一个习惯： 每一次只能跳1步或跳3步，试问猴子通过这个阶梯有多少种不同的跳跃方式？

输入描述:
输入只有一个整数N（0<N<=50）此阶梯有多少个阶梯
输出描述:
输出有多少种跳跃方式（解决方案数）

示例1：
输入
50
输出
122106097

示例2：
输入
3
输出
2
'''
def seven(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    ans = 0
    if n > 3:
        ans = seven(n - 1) + seven(n - 3)
    return ans


print(seven(1))
print(seven(2))
print(seven(3))
print(seven(4))
print(seven(10))
print(seven(50))

'''
8、分糖果    贪心
小明从糖果盒中随意抓一把糖果，每次小明会取出一半的糖果分给同学们。
当糖果不能平均分配时，小明可以选择从糖果盒中（假设盒中糖果足够）取出一个糖果或放回一个糖果。
小明最少需要多少次（取出、放回和平均分配均记一次），能将手中糖果分至只剩一颗

输入描述:
抓取的糖果数（<10000000000）：
15
输出描述:
最少分至一颗糖果的次数：
5

示例1：
输入
15
输出
5
备注:
解释：(1)15+1=16;(2)16/2=8;(3)8/2=4;(4)4/2=2;(5)2/2=1;
'''
def eight(n, t, tl = []):
    if n == 1:
        tl.append(t)
        return t
    if n % 2 == 0:
        eight(n / 2, t + 1, tl)
    else:
        eight(n + 1, t + 1, tl)
        eight(n - 1, t + 1, tl)

# eight(1)
# eight(15)
# eight(98867)
res = []
eight(1, 0, res)
print(res)
print(min(res))

'''
9、报数游戏    链表
100个人围成一圈，每个人有一个编码，编号从1开始到100。他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，直到剩余的人数小于M。请问最后剩余的人在原先的编号为多少？

输入描述:
输入一个整数参数M
输出描述:
如果输入参数M小于等于1或者大于等于100，输出“ERROR!”；否则按照原先的编号从小到大的顺序，以英文逗号分割输出编号字符串

示例1：
输入
3
输出
58,91
说明
输入M为3，最后剩下两个人
示例2：
输入
4
输出
34,45,97
说明
输入M为4，最后剩下三个人
'''
def nine(m):
    if m <= 1 or m >= 100:
        return 'ERROR!'
    ans = []
    for i in range(100):
        ans.append(i + 1)
    index = count = 0
    while len(ans) >= m:
        count += 1
        if count == m:
            ans.pop(index)
            count = 0
            if index > len(ans) - 1:
                index = 0
        else:
            if index == len(ans) - 1:
                index = 0
            else:
                index += 1
    ans = list(map(str, ans))
    return ans

print(nine(3))
print(nine(4))
print(nine(1))


'''
10、消消乐游戏    栈
游戏规则：输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。
在字符串上反复执行消除的动作，直到无法继续消除为止，此时游戏结束。
输出最终得到的字符串长度。

输入描述:
输入原始字符串 str ，只能包含大小写英文字母，字母的大小写敏感， str 长度不超过100。
输出描述:
输出游戏结束后，最终得到的字符串长度


示例1
输入
gg
输出
0
说明
gg 可以直接消除，得到空串，长度为0
示例2
输入
mMbccbc
输出
3
说明
在 mMbccbc 中，可以先消除 cc ；此时字符串变成 mMbbc ，可以再消除 bb ；此时字符串变成 mMc ，此时没有相邻且相同的字符，无法继续消除。最终得到的字符串为 mMc ，长度为3
备注:
输入中包含 非大小写英文字母 时，均为异常输入，直接返回 0
'''
def ten(string):
    sl = list(map(str,string))
    nsl = []
    # for i in sl:
    #     if nsl and nsl[-1]  == i:
    #         nsl.pop()
    #     else:
    #         nsl.append(i)
    for i in sl:
        if len(nsl) > 0:
            if i == nsl[-1]:
                nsl.pop()
            else:
                nsl.append(i)
        else:
            nsl.append(i)
    return len(nsl)


print(ten('gg'))
print(ten('mMbccbc'))
