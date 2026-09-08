class Solution:
    def isPalindrome(self, s: str) -> bool:
        _str = []
        for ch in s:
            if ch.isalnum():
                _str.append(ch.lower())
        return _str == _str[::-1]        