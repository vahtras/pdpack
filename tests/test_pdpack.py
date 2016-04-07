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
        asi = pdpack.dsptsi(2, asp)
        numpy.testing.assert_allclose(asi, [[1., 2.], [2., 3.]])

    def test_unpack_antisym(self):
        asp = numpy.array([1., 2., 3.])
        asi = pdpack.daptge(2, asp)
        numpy.testing.assert_allclose(asi, [[1., -2.], [2., 3.]])

if __name__ == "__main__":
    unittest.main()
