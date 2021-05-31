class Solution:
    def isValid(self, s: str) -> bool:
        left = list()
        for i in s:
            if i == "(" or i == "[" or i == "{":
                left.append(i)
            else:
                if len(left) == 0:
                    return False
                if i == ")":
                    if left[-1] != "(":
                        return False
                    else:
                        left.pop()
                elif i == "]":
                    if left[-1] != "[":
                        return False
                    else:
                        left.pop()
                elif i == "}":
                    if left[-1] != "{":
                        return False
                    else:
                        left.pop()
        if len(left) == 0:
            return True
        else:
            return False
