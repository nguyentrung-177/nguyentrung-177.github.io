# Bài 1a. Hãy viết phương thức tìm số lượng các số nguyên âm
# trong một matrix đã được sắp xếp theo hàng và theo cột
# với độ phức tạp thuật toán là O(m*n)
import numpy as np

a = [[-11, -4, 3],
     [-4, -3.1, 6],
     [-2, 1.1, 9]]


def Find(matrix):
    m, n = np.shape(matrix)
    c = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < 0 and \
                    matrix[i][j] - np.round(matrix[i][j]) == 0:
                c += 1
    return c


print(Find(a))
