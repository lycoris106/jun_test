def f(nums):
    nums.sort()
    maxSum = 0
    l = len(nums)
    for i in range(0, l, 2):
        maxSum += nums[i]

    return maxSum

def main():
    print(f([6, 2, 6, 5, 1, 2]))


if __name__ == "__main__":
    main()