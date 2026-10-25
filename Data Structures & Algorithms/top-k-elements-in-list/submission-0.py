class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        distinctNums = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
                distinctNums.append(num)
            else:
                dic[num] += 1

        bucket = []
        for _ in range(len(nums)+1):
            bucket.append([])
        for num in distinctNums:
            freq = dic[num]
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
            if len(result) == k:
                return result
                