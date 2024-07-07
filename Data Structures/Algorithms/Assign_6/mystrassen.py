
import numpy as np

def strassen_algorithm(x, y):
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]

    p1 = strassen_algorithm(a, f - h)
    p2 = strassen_algorithm(a + b, h)
    p3 = strassen_algorithm(c + d, e)
    p4 = strassen_algorithm(d, g - e)
    p5 = strassen_algorithm(a + d, e + h)
    p6 = strassen_algorithm(b - d, g + h)
    p7 = strassen_algorithm(a - c, e + f)

    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[: m, : m] = p5 + p4 - p2 + p6
    result[: m, m:] = p1 + p2
    result[m:, : m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    return result[: n, : n]

if __name__ == "__main__":

    x = np.array([
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1] ])
                    
    y = np.array([
                    [-1, 0, 0], 
                    [0, -1, 0], 
                    [0, 0, -1] ])
                    
    print('Matrix multiplication result: ')
    print(strassen_algorithm(x, y))



# ------------------------------------------------------
# # Program to multiply two matrices using nested loops

# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]


# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)

# ----------------------------------------------------

# import numpy as np

# def split(matrix):
# 	"""
# 	Splits a given matrix into quarters.
# 	Input: nxn matrix
# 	Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
# 	"""
# 	row, col = 3 ,3
# 	row2, col2 = row//2, col//2
# 	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

# def strassen(x, y):
# 	"""
# 	Computes matrix product by divide and conquer approach, recursively.
# 	Input: nxn matrices x and y
# 	Output: nxn matrix, product of x and y
# 	"""

# 	# Base case when size of matrices is 1x1
# 	if len(x) == 1:
# 		return x * y

# 	# Splitting the matrices into quadrants. This will be done recursively
# 	# until the base case is reached.
# 	a, b, c, d = split(x)
# 	e, f, g, h = split(y)

# 	# Computing the 7 products, recursively (p1, p2...p7)
# 	p1 = strassen(a, f - h)
# 	p2 = strassen(a + b, h)	
# 	p3 = strassen(c + d, e)	
# 	p4 = strassen(d, g - e)	
# 	p5 = strassen(a + d, e + h)	
# 	p6 = strassen(b - d, g + h)
# 	p7 = strassen(a - c, e + f)

# 	# Computing the values of the 4 quadrants of the final matrix c
# 	c11 = p5 + p4 - p2 + p6
# 	c12 = p1 + p2		
# 	c21 = p3 + p4		
# 	c22 = p1 + p5 - p3 - p7

# 	# Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
# 	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

# 	return c

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]

# print(strassen(X,Y))

# ------------------------------------------------------

