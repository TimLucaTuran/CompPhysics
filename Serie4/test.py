import numpy as np
from himmelblau import himmelblau
lambda_ = 0.1
x_start = [1,1]
fhandle = himmelblau

simplex_list = np.zeros((3,3))
simplex_list[0][0] = x_start[0]
simplex_list[0][1] = x_start[1]
simplex_list[0][2] = fhandle(simplex_list[0][0], simplex_list[0][1])

# x1, x2 generieren
simplex_list[1][0] = x_start[0]+lambda_
simplex_list[1][1] = x_start[1]
simplex_list[1][2] = fhandle(simplex_list[1][0], simplex_list[1][1])

simplex_list[2][0] = x_start[0]
simplex_list[2][1] = x_start[1]+lambda_
simplex_list[2][2] = fhandle(simplex_list[2][0], simplex_list[2][1])
np.sort(simplex_list, axis=-1)
print(simplex_list)
