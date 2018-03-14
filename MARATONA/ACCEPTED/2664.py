"""
t, n, m = map(int, raw_input().split())
programs = 0
for vi in range(n, m+1):
    for ti in range(1, t):
        for d in range(t):
            vf = vi + ti - (2*d) - 1
            s = ti - d - 1
            if n <= vf <= m:
                print vi, vf, s, d
                programs = (programs + 1) % 1000000007

print programs
"""

t, n, m = map(int, raw_input().split())

m = m - n
n = 0

mat = [[-1 for i in range(m+1)] for j in range(t+1)]
for i in range(2):
    for j in range(m+1):
        if i == 0:
            mat[i][j] = 0
        elif i == 1:
            mat[i][j] = 1
for i in range(2, t+1):
    for j in range(m+1):
        if j == 0:
            mat[i][j] = mat[i-1][j+1] % 1000000007
        elif j == m: 
            mat[i][j] = mat[i-1][j-1] % 1000000007
        else:
            mat[i][j] = (mat[i-1][j-1] + mat[i-1][j+1]) % 1000000007

s = 0
for item in mat[-1]:
    s = (s + item) % 1000000007

print s