# Your task is to make two functions, max and min (maximum and minimum in PHP and Python, maxi and 
# mini in Julia) that take a(n) array/vector of integers list as input and outputs, respectively, 
# the largest and lowest number in that array/vector.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

print(minimum([-52, 56, 30, 29, -54, 0, -110]) == -110) 
print(minimum([42, 54, 65, 87, 0]) == 0)
print(minimum([1, 2, 3, 4, 5, 10]) == 1)
print(minimum([-1, -2, -3, -4, -5, -10]) == -10)
print(minimum([9]) == 9)

