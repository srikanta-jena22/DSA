class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c=[0]*26
        for i in range(len(s)):
            c[ord(s[i])-ord('a')]+=1
            c[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if c[i]!=0:
                return False
        return True
d = Solution()
print(d.isAnagram("anagram","nagaram"))
print(d.isAnagram("rat","car"))