class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: not x & 1,map(len,map(str,nums)))))
