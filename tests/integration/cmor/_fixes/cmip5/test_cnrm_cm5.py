import unittest

from cf_units import Unit
from iris.cube import Cube

from esmvalcore.cmor._fixes.cmip5.cnrm_cm5 import Msftmyz, Msftmyzba


class TestMsftmyz(unittest.TestCase):
    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0], var_name='msftmyz', units='J')
        self.fix = Msftmyz()

    def test_fix_data(self):
        cube = self.fix.fix_data(self.cube)
        self.assertEqual(cube.data[0], 1.0e6)
        self.assertEqual(cube.units, Unit('J'))


class TestMsftmyzba(unittest.TestCase):
    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0], var_name='msftmyzba', units='J')
        self.fix = Msftmyzba()

    def test_fix_data(self):
        cube = self.fix.fix_data(self.cube)
        self.assertEqual(cube.data[0], 1.0e6)
        self.assertEqual(cube.units, Unit('J'))
