class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        numSet = set(nums)

        def backtrack(path):
            if sum(path) == target:
                if sorted(path) not in results:
                    results.append(sorted(path[:]))
            
            for choice in numSet:
                if target - sum(path) < 0:
                    continue
                
                path.append(choice)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return results