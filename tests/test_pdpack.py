import unittest
import numpy
from . import pdpack


class PDTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_unpack(self):
        asp = numpy.array([1., 2., 3.])
        asi = numpy.zeros((2, 2), dtype='float64')
        asi = pdpack.dsptsi(asi, asp)
        numpy.testing.assert_allclose(asi, [[1., 2.], [2., 3.]])

if __name__ == "__main__":
    unittest.main()
