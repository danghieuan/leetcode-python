class Solution(object):
    def two_sum_bruce_force_solution(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return i, j
                # print(i, j)
    

sol = Solution()

# Test case 1
print(sol.two_sum_bruce_force_solution([2,7,11,15], 9))
# Test case 2
print(sol.two_sum_bruce_force_solution([3,2,4], 6))
# Test case 3
print(sol.two_sum_bruce_force_solution([3,3], 6))