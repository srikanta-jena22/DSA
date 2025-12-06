class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in d:
                return [d[diff],i]
            d[n]=i
o=Solution()
print(o.twoSum([2,7,11,15],9))
print(o.twoSum([3,2,4],6))
print(o.twoSum([3,3],6))

        