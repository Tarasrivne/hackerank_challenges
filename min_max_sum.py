def miniMaxSum(arr):
    arr.sort()
    sum_min = sum(arr[0:4])
    sum_max = sum(arr[1:5])
    print(f'{sum_min} {sum_max}')

a = miniMaxSum([1,3,5,7,9])
print(a)