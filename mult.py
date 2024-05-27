import torch

N = 368_403_150 + 1 # N*N(2N-1) > 10^26

matrix_1 = torch.rand(N, N)
matrix_2 = torch.rand(N, N)

result = torch.matmul(matrix_1, matrix_2)
