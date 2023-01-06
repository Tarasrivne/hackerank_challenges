def plusMinus(arr):

    p, m, z = [], [], []
    n = len(arr)
    for i in arr:
        if i > 0: # we define positive values
            p.append(i)
        elif i < 0: # we define negativee values
            m.append(i)
        else:
            z.append(i) # equal 0
    numbers = len(p), len(m), len(z)
    for i in numbers:
        print(round(i/n, 5)) # функція round показує числа після коми

a = plusMinus([1,1,-2,-2,0])
print(a)