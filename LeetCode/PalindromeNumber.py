class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) ==1 :
            return True
        if len(x) == 2:
            if(x[0] == x[1]):
                return True
            return False
        if len(x) == 3:
            if(x[0] == x[2]):
                return True
            return False
        size = len(x)//2
        #12345
        if(len(x)%2 == 0):
            xLeft = x[0:size]
            xRight = x[size:]
        else:
            xLeft = x[0:size]
            xRight = x[size+1:]
        if xLeft == xRight[::-1]:
            return True
        return False
