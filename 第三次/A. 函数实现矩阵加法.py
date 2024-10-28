import ast

rows, cols = map(int, input().split())

matrix1 = ast.literal_eval(input())
matrix2 = ast.literal_eval(input())

result = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]

print(str(result).replace(" ", ""))
