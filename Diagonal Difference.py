def diagonalDifference(arr):
    left_sum = 0
    right_sum = 0
    left_point = 0
    right_point = len(arr[0]) - 1
    for i in arr:
        left_number = i[left_point]  # 11
        right_number = i[right_point]  # 4

        left_sum += left_number
        right_sum += right_number

        left_point += 1
        right_point -= 1

    return abs(left_sum - right_sum)