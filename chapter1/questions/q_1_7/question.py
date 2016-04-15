class MatrixWithZero(object):
    def __init__(self, matrix):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
    def convert(self):
        self.__find_zero_places()
        self.__convert_rows_to_zero()
        self.__convert_cols_to_zero()
    def __find_zero_places(self):
        print 'haha'
        self.zero_rows = []
        self.zero_cols = []
        for r_i, row in enumerate(self.matrix):
            for c_i, cell in enumerate(row):
                if cell == 0:
                    self.zero_rows.append(r_i)
                    self.zero_cols.append(c_i)
    def __convert_rows_to_zero(self):
        for r_i in self.zero_rows:
            self.matrix[r_i] = [0] * self.n
    def __convert_cols_to_zero(self):
        for c_i in self.zero_cols:
            for row in self.matrix:
                row[c_i] = 0

# Test cases:

matrix = [
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,7],
    [1,2,3,4,5,6,0],
    [1,2,3,4,0,6,7]
]

matrix_with_zero = MatrixWithZero(matrix)
print matrix_with_zero.matrix
matrix_with_zero.convert()
print matrix_with_zero.matrix
