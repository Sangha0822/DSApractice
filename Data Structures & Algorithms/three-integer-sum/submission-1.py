class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNum = sorted(nums)
        left = 1
        right = len(nums)-1
        
        collect = []
        for i in range(len(sortedNum)):
            if i > 0 and sortedNum[i] == sortedNum[i - 1]:
                continue
            left = i+1
            right = len(sortedNum)-1
            while left < right:
                if sortedNum[i]+sortedNum[left]+sortedNum[right] < 0:
                    left += 1
                elif sortedNum[i]+sortedNum[left]+sortedNum[right] > 0:
                    right -= 1
                else:
                    collect.append([sortedNum[i],sortedNum[left],sortedNum[right]])
                    left += 1
                    right -= 1

                    while left < right and sortedNum[left] == sortedNum[left - 1]:
                        left += 1

                    while left < right and sortedNum[right] == sortedNum[right + 1]:
                        right -= 1
        return collect
            