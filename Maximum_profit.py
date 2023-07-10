class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def binary_search(target,left,right):
            
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][1] <= target : left = mid + 1
                else: right = mid - 1
            
            return right
        
        tam = len(profit)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(tam)]
        jobs.sort(key = lambda x: x[1])
        
        maximum_profit = [0]*tam
        for i in range(tam):
            
            searched = binary_search(jobs[i][0] , 0 , i - 1)
            sum = maximum_profit[searched] if searched != -1 else 0
            maximum_profit[i] = max(maximum_profit[i-1],jobs[i][2] + sum)

        return maximum_profit[-1]