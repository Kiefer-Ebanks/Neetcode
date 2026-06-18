class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val = False
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 1
            else:
                val = True

        return val
        