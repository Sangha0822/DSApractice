class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left = 0
        right = len(numbers)-1
        while left < right:
            find = target - numbers[right]
            if find < numbers[left]:
                right -= 1
            elif find > numbers[left]:
                left += 1
            else:
                return[left+1,right+1]