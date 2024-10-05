class Solution:
    def smallestSubsequence(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.smallestSubsequence(suffix.replace(char, ''))

        return ''