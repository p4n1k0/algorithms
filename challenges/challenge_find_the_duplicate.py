def find_duplicate(nums):
    if len(nums) < 1:
        False
    nums.sort()
    for index in range(len(nums) - 1):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]
    return False
