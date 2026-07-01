class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        nlen=len(strs)
        dp={};
        def helper(i,m,n):
            if i<0:    return 0;
            if (i,m,n) in dp:
                return dp[(i,m,n)];

            notselect=helper(i-1,m,n);
            mcount,ncount=strs[i].count('0'),strs[i].count('1');
            if(m>=mcount and n>=ncount):
                notselect=max(notselect,helper(i-1,m-mcount,n-ncount)+1); #select

            dp[(i,m,n)]=notselect;
            return notselect;
        return helper(nlen-1,m,n);
        
        