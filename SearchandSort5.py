def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
