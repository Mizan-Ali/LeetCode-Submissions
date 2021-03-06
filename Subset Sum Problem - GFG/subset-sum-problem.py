#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        arr.sort()
        global ans
        global dp
        ans = 0
        dp = {}
        
        def solve(idx, remsum):
            global ans
            global dp
            if idx == N:
                if remsum == 0:
                    return True
                return False
            if remsum == 0:
                return True
            if(idx, remsum) not in dp:
                if arr[idx] <= remsum:
                    # pick and skip
                    dp[(idx, remsum)] = solve(idx+1, remsum-arr[idx]) or solve(idx+1, remsum)
                else:
                    return False
            return dp[(idx, remsum)]
        
        return solve(0, sum)
         
        
        
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends