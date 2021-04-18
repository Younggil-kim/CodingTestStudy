class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -1*int((str(x)[1:])[::-1])
        else:
            x = int(str(x)[::-1])
        if x not in range(-2**31, 2**31 -1):
            x = 0
        return x
