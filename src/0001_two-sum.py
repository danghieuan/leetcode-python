# class Solution(object):
#     def two_sum_bruce_force_solution(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return i, j
#                 # print(i, j)
    

# sol = Solution()

# # Test case 1
# print(sol.two_sum_bruce_force_solution([2,7,11,15], 9))
# # Test case 2
# print(sol.two_sum_bruce_force_solution([3,2,4], 6))
# # Test case 3
# print(sol.two_sum_bruce_force_solution([3,3], 6))
# # Test case 4
# print(sol.two_sum_bruce_force_solution([], 6))



class Solution(object):
    def two_sum_using_two_pointer(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        nums = [2, 7, 11, 15], target = 9 --> result return output: [0, 1]
        left[i] + right[j] > target
        ---> reduce right[j-1]
        left[i] + right[j] < target
        ---> increment left[i+1]


        """


        # Wrong answer: 19 / 63 testcases passed
        left = 0 # start with index = 0
        right = len(sorted(nums)) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left +=1
            elif sum > target:
                right -=1
            else:
                return left, right
        return []
sol = Solution()

# Test case 1
print(sol.two_sum_using_two_pointer([2,7,11,15], 9))
# Test case 2
print(sol.two_sum_using_two_pointer([3,2,4], 6))