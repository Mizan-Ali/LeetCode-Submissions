#User function Template for python3

def rotate( arr, n):
    temp = arr[0]
    for i in range(1, n):
        temp2 = arr[i]
        arr[i] = temp
        temp = temp2
    arr[0] = temp
    return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends