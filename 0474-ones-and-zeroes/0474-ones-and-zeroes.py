class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        nlen=len(strs)
        dp={}
        for val in strs:
           mcount,ncount=val.count('0'),val.count('1');
           for i in range(m,mcount-1,-1):
            for j in range(n,ncount-1,-1):
                cal=dp.get((i,j),0) #not take
                if(i>=mcount and j>=ncount):
                    cal=max(cal,dp.get((i-mcount,j-ncount),0)+1) #take
                dp[(i,j)]=cal;
        return dp.get((m,n),0)



        # dp={};
        # def helper(i,m,n):
        #     if i<0:    return 0;
        #     if (i,m,n) in dp:
        #         return dp[(i,m,n)];

        #     notselect=helper(i-1,m,n);
        #     mcount,ncount=strs[i].count('0'),strs[i].count('1');
        #     if(m>=mcount and n>=ncount):
        #         notselect=max(notselect,helper(i-1,m-mcount,n-ncount)+1); #select

        #     dp[(i,m,n)]=notselect;
        #     return notselect;
        # return helper(nlen-1,m,n);
        
        