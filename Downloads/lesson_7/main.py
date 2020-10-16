
class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        ret_matrix = []
        for el_1, el_2 in zip(self.list, other.list):
            ret_matrix.append([x + y for x, y in zip(el_1, el_2)])

        return ret_matrix

    def __str__(self):
        self.list
        for line in self.list:
            print(line)


matrix_1 = Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix_1 + matrix_2)
