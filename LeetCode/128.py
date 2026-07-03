# 128. Longest Consecutive Sequence

# Brute
def longestConsecutive(nums):
    mx = 0
    for num in nums:
        count = 1
        x = num
        while x+1 in nums:
            count += 1
            x += 1
        mx = max(count,mx)
    return mx


# Better
def longestConsecutive(nums):
    nums.sort()
    longest = 0
    last_smaller = float("-inf")
    count = 0
    for num in nums:
        if num-1 == last_smaller:
            count += 1
            last_smaller = num
        elif num != last_smaller:
            count = 1
            last_smaller = num
        longest = max(longest,count)
    return longest


# Optimal
def longestConsecutive(nums):
    s = set(nums)
    longest = 0
    for num in s:
        if num-1 not in s:
            x = num
            count = 1
            while x+1 in s:
                count += 1
                x += 1
            longest = max(longest,count)



nums = [ int(i) for i in input("> ").split() ]
res = longestConsecutive(nums)
print("~"*15)
print("Result:",res)
print("~"*15)