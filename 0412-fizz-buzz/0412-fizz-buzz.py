class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        i = 1
        while i <= n:
            out = ''
            if i % 3 == 0:
                out += 'Fizz'
            if i % 5 == 0:
                out += 'Buzz'
            if out == '':
                out += str(i)
            ret.append(out)
            i += 1
        return ret