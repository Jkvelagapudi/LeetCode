# 1
class Solution(object):
    def twoSum(self, nums, target):
        final_array = []

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and len(final_array) == 0 and i != j:
                    final_array.append(i)
                    final_array.append(j)
                    

        return final_array