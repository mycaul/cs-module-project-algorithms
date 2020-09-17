'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
      # Your code here
    # when iterating over the input array, the expected value at the current iteration index needs to be the product of every number except at the current iteration index
    
    # size of array
    n = len(arr)

    # temp spots for left & right
    l = [0]*n
    r = [0]*n

    # temp spot for product of function
    p = [0]*n

    # leftmost element of array fixed to 1
    l[0] = 1

    # rightmost element of array fixed to 1
    r[n-1]=1
    
    # constructor for left subarray
    for i in range(1, n):
        l[i] = arr[i - 1] * l[i - 1]

    # contstructor for the right subarray 
    for j in range(n-2, -1, -1):
        r[j] = arr[j+1] * r[j+1]
    
    # constructor for the product array using the left & right subarrays
    for i in range(n):
        p[i] = l[i] * r[i]

    return p
if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
