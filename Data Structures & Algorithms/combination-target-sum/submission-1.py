class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        numSet = set(nums)

        def backtrack(path):
            if sum(path) == target:
                results.append(sorted(path[:]))
            
            for choice in numSet:
                if target - sum(path) < 0:
                    continue
                if sorted(path + [choice]) in results:
                    continue

                path.append(choice)
                backtrack(path)
                path.pop()
        
        backtrack([])
        return results