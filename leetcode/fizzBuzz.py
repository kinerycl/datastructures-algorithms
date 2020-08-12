class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_lst = []
        while n != 0:
            if n % 5== 0 and n%3 == 0:
                ret_lst.insert(0, 'FizzBuzz')
            elif n%5 == 0:
                ret_lst.insert(0, 'Buzz')
            elif n%3 == 0:
                ret_lst.insert(0, 'Fizz')
            else:
                ret_lst.insert(0, str(n))
            n-=1
        return ret_lst
