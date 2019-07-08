class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def read(word, num):
            if num == 1:
                return word
            else:
                new_word = ""
                i = 0
                while i < len(word):
                    letter = word[i]
                    count = 0
                    while i < len(word) and word[i] == letter:
                        i +=1
                        count += 1
                    new_word += str(count)
                    new_word += letter
                return read(new_word, num -1)
        if n == 0:
            return ""
        else:
            return read("1", n)
            
