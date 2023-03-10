#!/user/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
from typing import List

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        flag = [[0 for _ in range(n)] for _ in range(m)]
        # 处理第1列
        mflag = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                mflag = 0
            flag[i][0] = mflag
        # 处理第1行,对列数进行迭代
        nflag = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                nflag = 0
            flag[0][i] = nflag
        # 处理状态转移方程
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                flag[i][j] = flag[i - 1][j] + flag[i][j - 1]
        return flag[-1][-1]

    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        # 制作棋盘
        n = len(obstacleGrid)  # length of rows
        m = len(obstacleGrid[0])  # length of columns
        dp = [[0 for _ in range(m)] for _ in range(n)]
        # (0,0) 可能是障碍物
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        # 处理第1列
        for i in range(1, n):
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1
        # 处理第1行
        for j in range(1, m):
            if obstacleGrid[0][j] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
            else:
                dp[0][j] = 1
        # 状态转移方程
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    # 如果当前格子是障碍物
                    dp[i][j] = 0
                else:
                    # 路径总数来自于上方(dp[i-1][j])和左方(dp[i][j-1])
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


s = Solution()
# print(
#     s.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0]]))
print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))
print(s.uniquePathsWithObstacles(obstacleGrid=[[1]]))
