'''
Given nxm matrix on ints
0 1 2
1 2 3
1 4 5
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n == 1 or m == 1:
            return mat
        min_size = min(m, n)
        for i in range(m-1, -1, -1):
            vals = [mat[0][i]]
            x, y = 0, i
            for j in range(min_size):
                x += 1
                y += 1
                if x >= n or y >= m:
                    break
                vals.append(mat[x][y])
            vals.sort()
            x, y = 0, i
            for j in range(len(vals)):
                mat[x][y] = vals[j]
                x += 1
                y += 1
        for i in range(1, n):
            vals = [mat[i][0]]
            x, y = i, 0
            for j in range(min_size):
                x += 1
                y += 1
                if x >= n or y >= m:
                    break
                vals.append(mat[x][y])
            vals.sort()
            x, y = i, 0
            for j in range(len(vals)):
                mat[x][y] = vals[j]
                x += 1
                y += 1
        return mat