class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + '#' + word
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        currPos = 0

        while currPos < len(s):
            j = currPos

            while s[j] != '#':
                j += 1

            length = int(s[currPos:j])

            word = ""
            for i in range(j + 1, j + 1 + length):
                word += s[i]

            result.append(word)

            currPos = j + 1 + length

        return result