class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        for i in range(len(position)):
            dic[position[i]] = speed[i]
        newPosition = sorted(position, reverse=True)

        for i in range(len(position)):
            speed[i] = dic[newPosition[i]]            
        
        stack = []
        for i in range(len(position)):
            time = (target-newPosition[i]) / speed[i]
            stack.append(time)
        
        cnt = 0
        prev = 0
        for curr in stack:
            if curr > prev:
                cnt += 1
                prev = curr
        return cnt