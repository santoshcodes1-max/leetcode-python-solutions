class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans=0
        n=len(nums)
        prefixCount=[0]*(n+1);
        for i,val in enumerate(nums):
            if val==target:
                prefixCount[i+1]=prefixCount[i]+1
            else:   prefixCount[i+1]=prefixCount[i];
        for i in range(n):
            for j in range(i,n):
                count=prefixCount[j+1]-prefixCount[i]
                sublength=(j-i+1)//2;
                if(count>sublength):    ans+=1;
        return ans;
        