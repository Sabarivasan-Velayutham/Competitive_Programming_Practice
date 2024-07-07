

# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/solutions/1865568/c-python-js-simple-explained-o-n-faster-than-100/

def countHillValley(nums):
    ans = 0
    final = [nums[0]]
    tmp = nums[0]

    # to prevent ADJACENT element duplication 
    for i in range(1,len(nums)) :
        if tmp != nums[i]:
            final.append(nums[i])
        tmp = nums[i]
    print(final)

    for i in range(1,len(final)-1):
        if (final[i] > final[i-1] and final[i] > final[i+1]) or (final[i] < final[i-1] and final[i] < final[i+1]):
            ans += 1

    return ans

print(countHillValley([5,7,7,1,7]))
print(countHillValley([2,4,1,1,6,5]))
print(countHillValley([6,6,5,5,4,1]))
