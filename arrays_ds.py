def reverse_array(a):
    # Write your code here
    list_reversed = []
    lenght_of_a = len(a)
    for index in range(lenght_of_a):
        # [1,2,3]
        reversed_index = lenght_of_a - index
        reversed_index_adjusted = reversed_index - 1
        list_reversed.append(a[reversed_index_adjusted])
    return list_reversed

# assert reverse_array([3,5,7])== [7,5,3], 'revese_array failed'
# assert  reverse_array([4,3,2,5]) == [5,2,3,4]

