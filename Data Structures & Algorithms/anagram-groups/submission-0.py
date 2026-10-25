class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))    
            dic[sortedWord].append(word)
        return list(dic.values())