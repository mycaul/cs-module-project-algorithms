'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #Your code here
    # set(arr) gives list of elements in array w/o dupls
    #  sum of the unique elements in the array times to
    #minus the sum of the array
    # what's left over is the odd-number-out
    return 2 * sum(set(arr)) - sum(arr)



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")