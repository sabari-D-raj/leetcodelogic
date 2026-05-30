class Solution:
    def romanToInt(self, s: str) -> int:
        dicts={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        text=list(s)
        for i, n in enumerate(text):
            current=n
            if i<len(text)-1:
                next = text[i+1]
            else:
                next=text[i] 
            if dicts.get(current) >= dicts.get(next):
                result+=dicts.get(current)
            if dicts.get(current)<dicts.get(next):
                result-=dicts.get(current)

        return result
