from skc_operator import *
from skc_utils import *

import math
import unittest

class TestUtils(unittest.TestCase):

	# Test that fowler_distance is independent of a global phase
	def test_fowler_distance(self):
		dist = fowler_distance(H.matrix, H.matrix)
		assert_approx_equals_tolerance(dist, 0, TOLERANCE9)

		# Shift by a global phase
		H2 = numpy.exp(1.0j*math.pi / 2) * H.matrix
		
		dist = fowler_distance(H2, H.matrix)
		assert_approx_equals_tolerance(dist, 0, TOLERANCE9)
		
	def test_n_from_epsilon(self):
		c_approx = 4*math.sqrt(2)
		eps_0 = 1.0 / 33.0
		n = n_from_eps(eps=0.0001, c_approx=c_approx, eps_0=eps_0)
		self.assertEqual(n, 13, "level of recursion was: " + str(n) + " but should be 13")
		
def get_suite():
	suite = unittest.TestSuite()
	loader = unittest.TestLoader()
	suite1 = loader.loadTestsFromTestCase(TestUtils)
	suite.addTest(suite1)
	return suite

if (__name__ == '__main__'):
	suite = get_suite()
	unittest.TextTestRunner(verbosity=3).run(suite)
