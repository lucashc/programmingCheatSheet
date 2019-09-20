# Floyd-Warshall's algorithm
## \note The object dist is a weighted adjacency matrix
def floyd_warshall(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
