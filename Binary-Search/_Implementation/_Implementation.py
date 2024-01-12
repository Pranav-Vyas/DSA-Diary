
# Iterative

def search(nums, target):
    i = 0
    j = len(nums)-1
    while i <= j:
        mid = (i+j)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid-1
        else:
            i = mid+1
    return -1

# Recursive

def bs(nums,i,j,target):
    if i>j:
        return -1
    mid = (i+j)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return bs(nums,i,mid-1,target)
    else:
        return bs(nums,mid+1,j,target)


def search(nums: [int], target: int):
    return bs(nums,0,len(nums)-1,target)
