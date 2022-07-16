x = 1
y = 1
z = 1
n = 2
result = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if n != i+j+k:
                result.append([i,j,k])
print(result)

# iterated through each character one by one