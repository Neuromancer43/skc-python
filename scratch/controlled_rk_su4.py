from skc.operator import *
from skc.dawson import *
from skc.group_factor import *
from skc.compose import *
from skc.basis import *
import math
import time

H4 = get_hermitian_basis(d=4)
theta = math.pi / 4 # 45 degrees

axis = pick_random_axis(H4)
# Compose a unitary to compile
matrix_U = matrixify([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,numpy.exp(1j * math.pi / 128)]])
op_U = Operator(name="U", matrix=matrix_U)

n = 4 
print("U= " + str(matrix_U))
print("n= " + str(n))

# Prepare the compiler
sk_set_factor_method(aram_diagonal_factor)
sk_set_basis(H4)
# We don't need this for Aram's factoring method
#sk_set_axis(X_AXIS)
sk_build_tree("su4", 6)

begin_time = time.time()

Un = solovay_kitaev(op_U, n)

compile_time = time.time() - begin_time

print("Compile Time: " + str(compile_time))
print("Approximated U: " + str(Un))

print("Un= " + str(Un.matrix))
print("len(Un)= " + str(len(Un.ancestors)))

print("trace_dist(U,Un)= " + str(trace_distance(Un.matrix, op_U.matrix)))
print("fowler_dist(U,Un)= " + str(fowler_distance(Un.matrix, op_U.matrix)))
