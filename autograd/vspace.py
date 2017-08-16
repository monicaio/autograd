from __future__ import absolute_import
import numpy as np
import numpy.random as npr
from .tracer import primitive, isbox

class VSpace(object):
    __slots__ = []
    iscomplex = False
    def __init__(self, value): pass

    def zeros(self):          assert False
    def ones(self):           assert False
    def standard_basis(self): assert False
    def randn(self):          assert False

    @primitive
    def add(self, x_prev, x_new):     return self._add(x_prev, x_new)
    @primitive
    def mut_add(self, x_prev, x_new): return self._mut_add(x_prev, x_new)
    @primitive
    def scalar_mul(self, x, a):       return self._scalar_mul(x, a)
    @primitive
    def inner_prod(self, x, y):       return self._inner_prod(x, y)
    @primitive
    def covector(self, x):            return self._covector(x)

    def _add(self, x, y):        return x + y
    def _mut_add(self, x, y):    x += y; return x
    def _scalar_mul(self, x, a): return x * a
    def _inner_prod(self, x, y): assert False
    def _covector(self, x):      return x

    def __eq__(self, other):
        return type(self) == type(other) and self.__dict__ == other.__dict__

    def __repr__(self):
        return "{}_{}".format(type(self).__name__, self.__dict__)

    def examples(self):
        # Used for testing only
        N = self.size
        unit_vect = np.zeros(N)
        unit_vect[npr.randint(N)] = 1.0
        unit_vect = self.unflatten(unit_vect)
        rand_vect = npr.randn(N)
        return [self.zeros(), self.unflatten(npr.randn(N))]

def vspace_flatten(value, covector=False):
    return vspace(value).flatten(value, covector)

def vspace(value):
    try:
        return vspace_mappings[type(value)](value)
    except KeyError:
        if isbox(value):
            return value._node.vspace
        else:
            raise TypeError("Can't find vspace for type {}".format(type(value)))

vspace_mappings = {}
def register_vspace(vspace_maker, value_type):
    vspace_mappings[value_type] = vspace_maker

def assert_vspace_match(x, expected_vspace):
    assert expected_vspace == vspace(x), \
        "\nGrad returned unexpected vector space" \
        "\nVector space is {}" \
        "\nExpected        {}".format(vspace(x), expected_vspace)