def find132pattern(nums):
    n = len(nums)
    stack = []
    second = float('-inf')

    for i in range(n - 1, -1, -1):
        if nums[i] < second:
            return True
        while stack and stack[-1] < nums[i]:
            second = stack.pop()
        stack.append(nums[i])

    return False
nums = [1, 2, 3, 4]
print(find132pattern(nums))

nums = [3,1,4,2]
print(find132pattern(nums))