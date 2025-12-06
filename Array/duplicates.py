class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

d = Solution()
print(d.containsDuplicate([1, 2, 3, 1]))
