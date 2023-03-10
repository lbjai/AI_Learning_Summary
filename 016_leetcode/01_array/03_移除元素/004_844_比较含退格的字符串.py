#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：s = "ab#c", t = "ad#c"
输出：true
解释：s 和 t 都会变成 "ac"。
示例 2：

输入：s = "ab##", t = "c#d#"
输出：true
解释：s 和 t 都会变成 ""。
示例 3：

输入：s = "a#c", t = "b"
输出：false
解释：s 会变成 "c"，但 t 仍然是 "b"。
 

提示：

1 <= s.length, t.length <= 200
s 和 t 只含有小写字母以及字符 '#'


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        todo: 待完善
        双指针
        :param s:
        :param t:
        :return:
        """
        i, j = len(s) - 1, len(t) - 1
        sk = tk = 0

        def two_handle(i, sk):
            while i >= 0:
                if s[i] == '#':
                    sk += 1
                    i -= 1
                elif sk > 0:
                    sk -= 1
                    i -= 1
                else:
                    break

        while i >= 0 or j >= 0:
            two_handle(i, sk)
            two_handle(j, tk)
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True

    def backspaceCompare_v1(self, s: str, t: str) -> bool:
        """
        栈技术 重构字符串  思路及算法

        最容易想到的方法是将给定的字符串中的退格符和应当被删除的字符都去除，
        还原给定字符串的一般形式。然后直接比较两字符串是否相等即可。
        :param s:
        :param t:
        :return:
        """

        # 时间复杂度：O(N+M)，其中 N 和 M 分别为字符串 S 和 T 的长度。我们需要遍历两字符串各一次。
        # 空间复杂度：O(N+M)，其中 N 和 M 分别为字符串 S 和 T 的长度。主要为还原出的字符串的开销。

        def get_str(s: str) -> str:
            """
            具体地，我们用栈处理遍历过程，每次我们遍历到一个字符：
            如果它是退格符，那么我们将栈顶弹出；
            如果它是普通字符，那么我们将其压入栈中。
            :param s:
            :return:
            """
            res = []
            for es in s:
                if es != '#':
                    res.append(es)
                elif res:
                    res.pop()
            return ''.join(res)

        return get_str(s) == get_str(t)


s = "a#b#c"
t = "ad##c"
so = Solution()
print(so.backspaceCompare(s, t))
