class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        #do again
        results = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                results.append(text[i+2])
        return results