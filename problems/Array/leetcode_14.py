class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)  # short = "flow"
        for item in strs:  # When item = "flight"
            while len(short) > 0:
                if item.startswith(short):
                    break
                else:
                    short = short[:-1]
        return short
