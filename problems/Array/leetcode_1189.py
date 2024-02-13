class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countChar = Counter(text)
        loon = Counter('balloon')
        result = len(text)
        for i in loon:
            result = min(result,countChar[i] // loon[i])

        return result    


        