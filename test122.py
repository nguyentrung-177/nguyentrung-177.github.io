# Bài 1b. Hãy viết phương thức tìm số lượng các số nguyên âm
# trong một matrix đã được sắp xếp theo hàng và theo cột
# với độ phức tạp thuật toán là O(m+n)
import numpy as np

a = [[-11, -4, -3],
     [-2, 1, 2],
     [-1, 1, 9]]
m, n = np.shape(a)


def find_index(arr):
    c = 0
    m, n = np.shape(arr)
    i = 0
    j = n - 1
    while (j >= 0
           and i < n):
        if arr[i][j] < 0:
            c += j + 1
            i += 1
        else:
            j -= 1
    return c


print(find_index(a))
