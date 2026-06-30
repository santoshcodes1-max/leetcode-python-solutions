class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        a,b,c,i=-1,-1,-1,0;
        while(i<n):
            if s[i]=='a':
                a=i;
            elif s[i]=='b':
                b=i;
            elif s[i]=='c':
                c=i;
            ans+=1+min(a,b,c);
            i+=1;
        return ans
        # for i in range(n):
        #     for j in range(n):
        #         if 'a' in s[i:j+1] and 'b' in s[i:j+1] and 'c' in s[i:j+1]:
        #             ans+=1;
        # return ans;
        