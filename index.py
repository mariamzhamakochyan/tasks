def index(nums, target):
    if target not in nums:
        for i in range(len(nums)):
            if nums[-1] < target:
                return len(nums)
            if nums[i] > target:
                return i
    elif target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return i


nums = [1, 2, 4, 5]
target = 3
print(index(nums, target))
