class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * 26
        visited = [0] * 26

        # Count frequency
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        stack = []

        for ch in s:
            idx = ord(ch) - ord('a')
            count[idx] -= 1

            if visited[idx]:
                continue

            while (len(stack) > 0 and
                   ch < stack[-1] and
                   count[ord(stack[-1]) - ord('a')] > 0):

                visited[ord(stack[-1]) - ord('a')] = 0
                stack.pop()

            stack.append(ch)
            visited[idx] = 1

        result = ""
        for ch in stack:
            result += ch

        return result