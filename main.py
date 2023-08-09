class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        
        for el in patterns :
            pos = word.find(el)
            if pos != -1 :
                counter += 1
        
        return counter