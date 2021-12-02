nums = [
    5208,
    5181,
    5161,
    5162,
    5164,
    5189,
    5190,
    5170,
]


three_window_sums = [nums[i - 2] + nums[i - 1] + nums[i] for i in range(len(nums)) if i >= 2]

num_increments = 0

for i, n in enumerate(three_window_sums):
    if i != 0:
        if n > three_window_sums[i - 1]:
            print(n)
            num_increments += 1

print(num_increments)
