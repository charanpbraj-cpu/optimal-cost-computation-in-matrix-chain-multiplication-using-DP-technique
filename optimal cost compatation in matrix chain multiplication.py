def matrix_chain_order(p):
    n = len(p) - 1

    m = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n]



p = [10, 20, 30, 40, 30]

print("Minimum number of scalar multiplications:", matrix_chain_order(p))