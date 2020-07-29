class Solution(object):
    def __init__(self):
        self.index = 0
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = []
        strings = []
        curr = ''
        index = 0
        
        while index < len(s):
            if s[index].isnumeric():
                count = 0
                while s[index].isnumeric():
                    count = count * 10 + int(s[index])
                    index +=1
                counts.append(count)
            elif s[index] == '[':
                strings.append(curr)
                curr = ''
                index +=1
            elif s[index] == ']':
                temp = strings.pop()
                count = counts.pop()
                for i in range(count):
                    temp += curr
                curr = temp
                index +=1
            else:
                curr += s[index]
                index +=1
            
        return curr
        
