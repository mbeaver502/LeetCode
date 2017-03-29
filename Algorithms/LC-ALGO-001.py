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
#   Change Log
#
#       2017 03 28  Initial version.
#                   Corrected to disallow non-distinct elements.
#-------------------------------------------------------------

def twoSum(_nums, _target, find_all=False):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []

    # A hideous way to get around negatives
    #   -- assuming _all_ of _nums is negative
    if _target < 0:
        target = _target * -1
        nums = [x * -1 for x in _nums]
    else:
        target = _target
        nums = _nums
    
    if len(nums) > 1:
        idx = 0

        # O(n), where n = # of items in nums
        while idx < len(nums) - 1:
            n = nums[idx]
            candidate = None

            # We'll try to find the delta in our list
            if target > n:
                delta = target - n
            else:
                delta = n - target
                
            # If we can't index the delta, then no solution
            # We slice down the list, meaning we'll never
            # need to check if the indices are equivalent
            try:
                offset = idx+1
                candidate = nums[offset:].index(delta) + offset

            except ValueError:
                pass

            if candidate:
                result.append([idx, candidate])

                if not find_all:
                    if len(result) > 0: result = result[0]
                    break
            
            idx += 1

    return result

#-------------------------------------------------------------

if __name__ == '__main__':
    #nums = [15, 4, 10, 18, 7, 13, 5, 14, 2, 6, 19, 9, 8, 11, 12, 16, 17, 20, 3, 1]
    nums = [-1, -2, -3, -4, -5]
    target = -8

    solutions = twoSum(nums, target, True)
    print solutions

    # Assuming array-of-arrays returned
#    for sol in solutions:
#        print '{} + {} = {}'.format(nums[sol[0]], nums[sol[1]], target)
