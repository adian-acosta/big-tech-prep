class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        hashmap = {}

        # loop through the elements of the list
        for index in range(len(nums)):
            # save the complement of the target with the current element
            complement = target - nums[index]

            # if the complement is in the hashmap return its index, otherwise add it to the map
            if complement in hashmap:
                return [hashmap[complement], index]
            else:
                hashmap[nums[index]] = index
        
        # found no solution
        return []

# https://leetcode.com/problems/two-sum/submissions/1623791324