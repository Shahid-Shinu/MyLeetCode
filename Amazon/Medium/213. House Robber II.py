class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return max(nums)

        nums1 = nums[1:]
        nums2 = nums[:-1]

        def rob_algo(nums):
            n = len(nums)
            dp = [0 for i in range(n)]
            
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
            return dp[n-1]
        
        return max(rob_algo(nums1), rob_algo(nums2))

