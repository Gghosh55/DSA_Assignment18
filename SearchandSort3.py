def isBadVersion(version):
    # Implementation of the isBadVersion API
    # Return True if the version is bad, False otherwise
    return version >= 4


def firstBadVersion(n):
    start = 1
    end = n

    while start < end:
        mid = start + (end - start) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1

    return start


n = 5
first_bad = firstBadVersion(n)
print(first_bad)
