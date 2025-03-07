n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = [int(element) for element in input().split(" ")]
    matrix.append(row)
result = [i * 2 for row in matrix for i in row]
print(result)
