import autograd.numpy as np
import autograd.numpy.random as npr
from test_util import *
from autograd import grad
npr.seed(1)

def test_dot():
    def fun( x, y): return to_scalar(np.dot(x, y))
    def dfun(x, y): return to_scalar(grad(fun)(x, y))

    mat1 = npr.randn(10, 11)
    mat2 = npr.randn(10, 11)
    vect1 = npr.randn(10)
    vect2 = npr.randn(11)
    vect3 = npr.randn(11)

    check_grads(fun, mat1, vect2)
    check_grads(fun, mat1, mat2.T)
    check_grads(fun, vect1, mat1)
    check_grads(fun, vect2, vect3)
    check_grads(dfun, mat1, vect2)
    check_grads(dfun, mat1, mat2.T)
    check_grads(dfun, vect1, mat1)
    check_grads(dfun, vect2, vect3)

def test_dot_with_floats():
    def fun( x, y): return to_scalar(np.dot(x, y))
    def dfun(x, y): return to_scalar(grad(fun)(x, y))

    mat1 = npr.randn(10, 11)
    vect1 = npr.randn(10)
    float1 = npr.randn()

    check_grads(fun, mat1, float1)
    check_grads(fun, float1, mat1)
    check_grads(fun, vect1, float1)
    check_grads(fun, float1, vect1)
    check_grads(dfun, mat1, float1)
    check_grads(dfun, float1, mat1)
    check_grads(dfun, vect1, float1)
    check_grads(dfun, float1, vect1)

def test_dot_method():
    def fun(x, y): return to_scalar(x.dot(y))

    mat1 = npr.randn(10, 11)
    mat2 = npr.randn(10, 11)
    vect1 = npr.randn(10)
    vect2 = npr.randn(11)
    vect3 = npr.randn(11)

    check_grads(fun, mat1, vect2)
    check_grads(fun, mat1, mat2.T)
    check_grads(fun, vect1, mat1)
    check_grads(fun, vect2, vect3)

def test_outer():
    def fun( x, y): return to_scalar(np.outer(x, y))
    def dfun(x, y): return to_scalar(grad(fun)(x, y))

    vect2 = npr.randn(11)
    vect3 = npr.randn(11)

    check_grads(fun, vect2, vect3)
    check_grads(fun, vect2.T, vect3)
    check_grads(fun, vect2.T, vect3.T)
    check_grads(dfun, vect2, vect3)
    check_grads(dfun, vect2.T, vect3)
    check_grads(dfun, vect2.T, vect3.T)


def test_max():
    def fun(x): return to_scalar(np.max(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_max_axis():
    def fun(x): return to_scalar(np.max(x, axis=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(3, 4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_max_axis_keepdims():
    def fun(x): return to_scalar(np.max(x, axis=1, keepdims=True))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(3, 4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_min():
    def fun(x): return to_scalar(np.min(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_min_axis():
    def fun(x): return to_scalar(np.min(x, axis=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(3, 4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_min_axis_keepdims():
    def fun(x): return to_scalar(np.min(x, axis=1, keepdims=True))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(3, 4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_sum_1():
    def fun(x): return to_scalar(np.sum(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_sum_2():
    def fun(x): return to_scalar(np.sum(x, axis=0))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_sum_3():
    def fun(x): return to_scalar(np.sum(x, axis=0, keepdims=True))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_cumsum():
    def fun(x): return to_scalar(np.cumsum(x, axis=0))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_cumsum_1d():
    def fun(x): return to_scalar(np.cumsum(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_cumsum_no_axis():
    def fun(x): return to_scalar(np.cumsum(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_non_numpy_sum():
    def fun(x, y):
        return to_scalar(sum([x, y]))
    d_fun = lambda x, y : to_scalar(grad(fun)(x, y))
    mat1 = npr.randn(10, 11)
    mat2 = npr.randn(10, 11)
    check_grads(fun, mat1, mat2)
    check_grads(d_fun, mat1, mat2)

def test_mean_1():
    def fun(x): return to_scalar(np.mean(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_mean_2():
    def fun(x): return to_scalar(np.mean(x, axis=0))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_mean_3():
    def fun(x): return to_scalar(np.mean(x, axis=0, keepdims=True))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 11)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_index_ints():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x[3, 0, 1])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_index_slice():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x[::-1, 2:4, :])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_index_lists():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x[[0, 1, 2], :, :])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_index_mixed():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x[3, 2:, [1, 3]])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_vector_slice():
    A = npr.randn(5)
    def fun(x): return to_scalar(x[2:4])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_index_slice_fanout():
    A = npr.randn(5, 6, 4)
    def fun(x):
        y = x[::-1, 2:4, :]
        z = x[::-1, 3:5, :]
        return to_scalar(y + z)
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_index_multiple_slices():
    A = npr.randn(7)
    def fun(x):
        y = x[2:6]
        z = y[1:3]
        return to_scalar(z)
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_reshape_method():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x.reshape((5 * 4, 6)))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_reshape_call():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(np.reshape(x, (5 * 4, 6)))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_ravel_method():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(x.ravel())
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_ravel_call():
    A = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(np.ravel(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_simple_concatenate():
    A = npr.randn(5, 6, 4)
    B = npr.randn(4, 6, 4)
    def fun(x): return to_scalar(np.concatenate((A, x)))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, B)
    check_grads(d_fun, B)

def test_concatenate_axis_0():
    A = npr.randn(5, 6, 4)
    B = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(np.concatenate((B, x, B)))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_concatenate_axis_1():
    A = npr.randn(5, 6, 4)
    B = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(np.concatenate((B, x, B), axis=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_concatenate_axis_1_unnamed():
    """Tests whether you can specify the axis without saying "axis=1"."""
    A = npr.randn(5, 6, 4)
    B = npr.randn(5, 6, 4)
    def fun(x): return to_scalar(np.concatenate((B, x, B), 1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_trace():
    def fun(x): return np.trace(x)
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 10)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_diag():
    def fun(x): return to_scalar(np.diag(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(10, 10)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_inv():
    def fun(x): return to_scalar(np.linalg.inv(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 8
    mat = npr.randn(D, D)
    mat = np.dot(mat, mat) + 1.0 * np.eye(D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_solve_arg1():
    D = 8
    A = npr.randn(D, D) + 10.0 * np.eye(D)
    B = npr.randn(D, D - 1)
    def fun(a): return to_scalar(np.linalg.solve(a, B))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, A)
    check_grads(d_fun, A)

def test_solve_arg2():
    D = 6
    A = npr.randn(D, D) + 1.0 * np.eye(D)
    B = npr.randn(D, D - 1)
    def fun(b): return to_scalar(np.linalg.solve(A, b))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    check_grads(fun, B)
    check_grads(d_fun, B)

def test_det():
    def fun(x): return np.linalg.det(x)
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 6
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_frobeneus_norm():
    def fun(x): return to_scalar(np.linalg.norm(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 6
    mat = npr.randn(D, D-1)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_transpose():
    def fun(x): return to_scalar(x.T)
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(8, 8)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_roll():
    def fun(x): return to_scalar(np.roll(x, 2, axis=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_roll_no_axis():
    def fun(x): return to_scalar(np.roll(x, 2, axis=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(4, 5)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

# TODO:
# squeeze, getitem
