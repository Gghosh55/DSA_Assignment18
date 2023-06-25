def merge_intervals(intervals):
    if not intervals:
        return []


    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:

            result[-1][1] = max(result[-1][1], interval[1])
        else:

            result.append(interval)

    return result
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
