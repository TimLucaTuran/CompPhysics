import numpy as np
from himmelblau import himmelblau
alpha_ = 1.0
lambda_ = 0.1
x_start = [1,1]
fhandle = himmelblau

simplex_list = np.zeros((3,3))
simplex_list[0][0:2] = x_start
simplex_list[0][2] = fhandle(simplex_list[0][0:2])

# x1, x2 generieren
simplex_list[1][0:2] = [x_start[0]+lambda_, x_start[1]]
simplex_list[1][2] = fhandle(simplex_list[1][0:2])

simplex_list[2][0:2] = [x_start[0], x_start[1]+lambda_]
simplex_list[2][2] = fhandle(simplex_list[2][0:2])
simplex_list.view('i8,i8,i8').sort(order=['f2'], axis=0)
mirror_center = 0.5 * (simplex_list[0][0:2]+simplex_list[1][0:2])
mirror_point = mirror_center + alpha_*(mirror_center-simplex_list[2][0:2])
print(mirror_point)
print(simplex_list)
print(np.var(simplex_list, axis=0)[2])
