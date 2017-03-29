#-------------------------------------------------------------
#   (c) 2017 J. Michael Beaver
#-------------------------------------------------------------
#   This code is distributed under the MIT License.
#
#   This code attempts to solve:
#       https://leetcode.com/problems/two-sum/
#       Given an array of integers, return indices of the two
#       numbers such that they add up to a specific target.
#
#   No claims are made on efficiency.
#
#   $> python -m cProfile LC-ALGO-001.py
#       31 function calls in 0.000 seconds (without I/O)
#-------------------------------------------------------------

def twoSum(nums, target, find_all=False):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    
    if len(nums) > 1:
        idx = 0

        # O(n), where n = # of items in nums
        for n in nums:

            # We'll try to find the delta in our list
            if target > n:
                delta = target - n
            else:
                delta = n - target

            # Unique elements only
            if n != delta:

                # If we can't index the delta, then no solution
                try:
                    result.append([idx, nums.index(delta)])
                except ValueError:
                    pass

                if not find_all:
                    if len(result) > 0: result = result[0]
                    break
            
            idx += 1

    return result

#-------------------------------------------------------------

if __name__ == '__main__':
    nums = [15, 4, 10, 18, 7, 13, 5, 14, 2, 6, 19, 9, 8, 11, 12, 16, 17, 20, 3, 1]
    target = 34

    solutions = twoSum(nums, target, True)

    for sol in solutions:
        print '{} + {} = {}'.format(nums[sol[0]], nums[sol[1]], target)
