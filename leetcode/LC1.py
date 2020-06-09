def twoSum(self, nums: List[int], target: int) -> List[int]:
    seenNumbers = {} # key: number, value: index
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seenNumbers:
            return [seenNumbers[diff], i]
        else:
            seenNumbers[nums[i]] = i