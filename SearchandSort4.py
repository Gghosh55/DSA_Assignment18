def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)
    buckets = list(nums)

    digit = 1
    while max_num // digit > 0:
        count = [0] * 10

        for num in buckets:
            count[(num // digit) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(buckets) - 1, -1, -1):
            digit_value = (buckets[i] // digit) % 10
            count[digit_value] -= 1
            index = count[digit_value]
            nums[index] = buckets[i]

        digit *= 10

    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i - 1])

    return max_diff
nums = [3, 6, 9, 1]
print(maximumGap(nums))
