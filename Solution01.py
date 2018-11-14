# Paul Gonzales
# ITEC2313
# 2018-11-13
# Solution 01

def greaterThan(ls, n):
    '''prints the elements in the list that are greater than n'''
    for i in range(len(ls)):
        if ls[i] > n:
            print(ls[i])
    return()

def main():
    nums = [1, 2, 3, 4, 5]
    
    greaterThan(nums, 3)
    
    return()

main()
