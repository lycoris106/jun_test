def f(nums, target):
    lbound = 0
    rbound = len(nums)-1

    while lbound <= rbound:
        mid = (lbound+rbound)//2
        if nums[mid] < target:
            lbound = mid+1
        elif nums[mid] > target:
            rbound = mid-1
        else:
            return mid
    return -1

def main():
    print(f([-1, 0, 4, 5, 15, 30], 10))


if __name__ == "__main__":
    main()