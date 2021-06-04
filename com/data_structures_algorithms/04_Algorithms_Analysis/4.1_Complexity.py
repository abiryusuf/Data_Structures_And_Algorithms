def total(n):
    totalSum = 0
    rowSum = 0
    matrix = 0
    for i in range(n):
        rowSum[i] = 0
        for j in range(n):
            rowSum[i] = rowSum[i] + matrix[i, j]
        totalSum = totalSum + rowSum[i]
    return totalSum

print(total([2, 4, 6, 8]))
