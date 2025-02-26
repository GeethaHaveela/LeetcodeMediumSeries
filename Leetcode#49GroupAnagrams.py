from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams=defaultdict(list) 

        for word in strs:
            sorted_word=tuple(sorted(word)) 
            anagrams[sorted_word].append(word)
        return list(anagrams.values()) 
s1=Solution()
print(s1.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))