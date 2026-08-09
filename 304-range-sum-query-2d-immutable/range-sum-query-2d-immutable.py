class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixes = []

        for i in range(len(matrix)):
            prefix = [0]

            for j in range(len(matrix[i])):
                prefix.append(prefix[-1] + matrix[i][j])

            self.prefixes.append(prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for i in range(row1, row2 + 1):
            total += self.prefixes[i][col2 + 1] - self.prefixes[i][col1]

        return total