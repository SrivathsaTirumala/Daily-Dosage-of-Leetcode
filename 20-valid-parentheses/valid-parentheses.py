class Solution:
    def isValid(self, s: str) -> bool:
        l=["()","[]","{}"]
        while True:
            flag=False
            for i in l:
                if i in s:
                    s=s.replace(i,"")
                    flag=True
            if not flag:
                break
        return len(s)==0
