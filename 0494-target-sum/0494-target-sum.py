class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dp={}
        def helper(nums,target, i):
            if(i<=0):
                if(target==0):
                    dp[(i,target)]=1
                    return 1; 
                return 0;
            if (i,target) in dp:    return dp[(i,target)];
            added=helper(nums,target+nums[i-1],i-1);
            subtract=helper(nums,target-nums[i-1],i-1);
            dp[(i,target)]=added+subtract;
            return dp[(i,target)];
        return helper(nums,target,n);

        