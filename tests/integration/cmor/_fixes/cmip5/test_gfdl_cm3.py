import unittest

from cf_units import Unit
from iris.cube import Cube

from esmvalcore.cmor._fixes.cmip5.gfdl_cm3 import Sftof


class TestSftof(unittest.TestCase):
    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0], var_name='sftof', units='J')
        self.fix = Sftof()

    def test_fix_data(self):
        cube = self.fix.fix_data(self.cube)
        self.assertEqual(cube.data[0], 100)
        self.assertEqual(cube.units, Unit('J'))
