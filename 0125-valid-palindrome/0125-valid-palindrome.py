class Solution(object):
    def isPalindrome(self, s):
        filtered = []

        for ch in s:
            # check a-z
            if 'a' <= ch <= 'z':
                filtered.append(ch)
            # check A-Z (convert manually to lowercase)
            elif 'A' <= ch <= 'Z':
                filtered.append(chr(ord(ch) + 32))
            # check 0-9
            elif '0' <= ch <= '9':
                filtered.append(ch)

        i = 0
        j = len(filtered) - 1

        while i < j:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1

        return True