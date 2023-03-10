#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


s = Solution()
print(s.fib(n=4))
