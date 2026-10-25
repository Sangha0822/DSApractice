class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1
        
        for letter in t:
            if letter not in dic:
                return False
            dic[letter] -= 1
            if dic[letter] == 0:
                del dic[letter]
        
        if dic:
            return False
        else:
            return True
        