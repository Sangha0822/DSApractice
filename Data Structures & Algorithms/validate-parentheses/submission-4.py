class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ['(', '{', '[']
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in valid:
                if char == '[':
                    stack.append(']')
                elif char == '(':
                    stack.append(')')
                else:
                    stack.append('}')
            else:
                if not stack:
                    return False
                else:
                    if char != stack.pop():
                        return False
        if stack:
            return False
        return True
