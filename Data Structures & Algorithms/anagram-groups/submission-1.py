class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = dict()
        for word in strs:
            sett = list(sorted(word))
            sett = "".join(sett)
            if sett not in dict1:
                dict1[sett] = [word]
            else:
                dict1[sett].append(word)

        return dict1.values()
        
        