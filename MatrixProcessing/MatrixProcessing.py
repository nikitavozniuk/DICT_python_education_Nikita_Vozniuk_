import copy

message = """
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
6. Inverse matrix
0. Exit
"""

transpose_variants = """
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
"""


class MatrixProcessing:
    result_matrix = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]

    def __init__(self, a, b=None, c=0):
        self.A = a
        self.B = b
        self.C = c

    @staticmethod
    def zeros_matrix(self, rows, cols):
        M = []
        while len(M) < rows:
            M.append([])
            while len(M[-1]) < cols:
                M[-1].append(0.0)

        return M

    @staticmethod
    def input_matrix():
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))

        matrix = []
        print("Enter the entries: ")

        for i in range(rows):
            a = []
            for j in range(columns):
                a.append(int(input()))
            matrix.append(a)

        return matrix

    def matrix_multiply(self):
        rows_a = len(self.A)
        cols_a = len(self.A[0])
        rows_b = len(self.B)
        cols_b = len(self.B[0])

        if cols_a != rows_b:
            raise ArithmeticError('Number of A columns must equal number of B rows.')

        result_matrix = MatrixProcessing.zeros_matrix(self, rows_a, cols_b)
        for i in range(rows_a):
            for j in range(cols_b):
                total = 0
                for ii in range(cols_a):
                    total += self.A[i][ii] * self.B[ii][j]
                result_matrix[i][j] = total
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                print(result_matrix[i][j], end=" ")
            print()

    def matrix_multiplication(self):
        cols = len(self.A)
        rows = len(self.A[0])

        for i in range(cols):
            for j in range(rows):
                self.A[i][j] *= self.C
        for i in range(cols):
            for j in range(rows):
                print(self.A[i][j], end=" ")
            print()

    def sum(self):
        try:
            if len(self.A) == len(self.B) and len(self.A[0]) == len(self.B[0]):
                for m in range(len(self.A)):
                    for n in range(len(self.B)):
                        self.result_matrix[m][n] = self.A[m][n] + self.B[m][n]
                for i in range(len(self.A)):
                    for j in range(len(self.A[0])):
                        print(self.result_matrix[i][j], end=" ")
                    print()
            else:
                raise ValueError('ERROR')
        except ValueError:
            print('ERROR')

    def copy_matrix(self, a):
        rows = len(a)
        cols = len(a)

        MC = self.zeros_matrix(self, rows, cols)

        for i in range(rows):
            for j in range(rows):
                MC[i][j] = a[i][j]

        return MC

    def transpose_main(self):
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                if i > j:
                    self.A[i][j], self.A[j][i] = self.A[j][i], self.A[i][j]
        print('The result is: ')
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                print(self.A[i][j], end=" ")
            print()

    def transpose_side(self):
        for i, n in zip(range(len(self.A)), range(len(self.A[0])-1, -1, -1)):
            for j, m in zip(range(len(self.A)), range(len(self.A[0])-1, -1, -1)):
                if j < n:
                    self.A[i][j], self.A[m][n] = self.A[m][n], self.A[i][j]
        print('The result is: ')
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                print(self.A[i][j], end=" ")
            print()

    def transpose_vertical(self):
        for i in range(len(self.A)):
            for j, m in zip(range(len(self.A)), range(len(self.A[0])-1, -1, -1)):
                if j < m:
                    self.A[i][j], self.A[i][m] = self.A[i][m], self.A[i][j]
        print('The result is: ')
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                print(self.A[i][j], end=" ")
            print()

    def transpose_horizontal(self):
        for j in range(len(self.A)):
            for i, n in zip(range(len(self.A)), range(len(self.A)-1, -1, -1)):
                self.A[i][j], self.A[n][j] = self.A[n][j], self.A[i][j]
        print('The result is: ')
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                print(self.A[i][j], end=" ")
            print()

    @staticmethod
    def identity_matrix(rows, cols):
        identity_m = [[None for y in range(rows)] for x in range(cols)]
        return identity_m

    def inverse(self):
        rows = len(self.A)
        cols = len(self.A[0])
        identity_m = [[None for y in range(rows)] for x in range(cols)]
        if det(self.A) == 0:
            print("This matrix doesn't have an inverse.")
            return
        for i in range(rows):
            for j in range(cols):
                tmp = minor(self.A, i, j)
                if i + j % 2 == 1:
                    identity_m[i][j] = -1 * det(tmp) / det(self.A)
                else:
                    identity_m[i][j] = 1 * det(tmp) / det(self.A)
        print('The result is: ')
        for i in range(len(identity_m)):
            for j in range(len(identity_m[0])):
                print(round(identity_m[i][j], 2), end=" ")
            print()


def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0

    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


def math_loop():
    answer = -1
    while answer != 0:
        print(message)
        answer = int(input('Your choice: '))

        if answer == 1:
            a = MatrixProcessing.input_matrix()
            b = MatrixProcessing.input_matrix()

            matrix_processing = MatrixProcessing(a, b)
            matrix_processing.sum()
            del matrix_processing
        elif answer == 2:
            a = MatrixProcessing.input_matrix()
            c = int(input('Enter number for multiply: '))

            matrix_processing = MatrixProcessing(a, None, c)
            matrix_processing.matrix_multiplication()
            del matrix_processing
        elif answer == 3:
            a = MatrixProcessing.input_matrix()
            b = MatrixProcessing.input_matrix()

            matrix_processing = MatrixProcessing(a, b)
            matrix_processing.matrix_multiply()
            del matrix_processing
        elif answer == 4:
            print(transpose_variants)
            transpose_type = int(input('Your choice: '))

            if transpose_type == 1:
                matrix = MatrixProcessing.input_matrix()

                matrix_processing = MatrixProcessing(matrix)
                matrix_processing.transpose_main()
            elif transpose_type == 2:
                matrix = MatrixProcessing.input_matrix()

                matrix_processing = MatrixProcessing(matrix)
                matrix_processing.transpose_side()
            elif transpose_type == 3:
                matrix = MatrixProcessing.input_matrix()

                matrix_processing = MatrixProcessing(matrix)
                matrix_processing.transpose_vertical()
            elif transpose_type == 4:
                matrix = MatrixProcessing.input_matrix()

                matrix_processing = MatrixProcessing(matrix)
                matrix_processing.transpose_horizontal()
        elif answer == 5:
            a = MatrixProcessing.input_matrix()

            print('The result is: {}'.format(det(a)))
        elif answer == 6:
            a = MatrixProcessing.input_matrix()

            matrix_processing = MatrixProcessing(a)
            matrix_processing.inverse()
        else:
            break


math_loop()

