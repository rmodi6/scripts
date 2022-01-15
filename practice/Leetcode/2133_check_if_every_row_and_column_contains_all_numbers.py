class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows, cols = [set(range(1, n+1)) for _ in range(n)], [set(range(1, n+1)) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j] not in rows[i] or matrix[i][j] not in cols[j]:
                    return False
                rows[i].remove(matrix[i][j])
                cols[j].remove(matrix[i][j])
        return True
