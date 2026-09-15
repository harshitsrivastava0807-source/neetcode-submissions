class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=[],s2=[]
        for i in range(len(s)):
            s1[i]=s[i]
            s2[i]=t[i]
        if s1==s2:
            return True