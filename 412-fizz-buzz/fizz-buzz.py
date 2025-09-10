class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            if i%3==0:
                res="Fizz"
                if i%5==0:
                    res+="Buzz"
            elif i%5==0:
                res="Buzz"
            else:
                res=str(i)
            l.append(res)
        return l