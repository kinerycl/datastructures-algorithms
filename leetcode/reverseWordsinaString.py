class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_lst = s.split()
        for i in range(len(word_lst)):
            word_lst[i] = word_lst[i][::-1]
        return string.join(word_lst)
