#BRUTE FORCE APPORACH
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]

#USING HASHING
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts=dict()
        for i ,n in enumerate(nums):
            differnce=target-n
            if differnce in dicts:
                return[dicts[differnce],i]
            dicts[n]=i
        return


        