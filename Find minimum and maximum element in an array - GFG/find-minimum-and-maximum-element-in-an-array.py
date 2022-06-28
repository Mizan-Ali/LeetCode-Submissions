#User function Template for python3

def getMinMax( a, n):
    Min, Max = float('inf'), float('-inf')
    for i in a:
        Min = min(Min, i)
        Max = max(Max, i)
    return Min, Max
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends