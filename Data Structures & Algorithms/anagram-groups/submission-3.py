class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in anagrams:
                anagrams[sortedword] = []
            anagrams[sortedword].append(word)
        
        return list(anagrams.values())