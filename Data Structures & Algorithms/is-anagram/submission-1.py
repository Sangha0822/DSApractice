class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))
        if new_s != new_t:
            return False
        return True