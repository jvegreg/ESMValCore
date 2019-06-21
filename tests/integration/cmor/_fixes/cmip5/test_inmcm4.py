"""Tests for inmcm4 fixes."""
import os
import shutil
import tempfile
import unittest

import iris
from iris.cube import Cube
from cf_units import Unit


from esmvalcore.cmor._fixes.cmip5.inmcm4 import Gpp, Lai, Nbp


class TestGpp(unittest.TestCase):
    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0], var_name='gpp', units='J')
        self.fix = Gpp()

    def test_fix_data(self):
        cube = self.fix.fix_data(self.cube)
        self.assertEqual(cube.data[0], -1)
        self.assertEqual(cube.units, Unit('J'))


class TestLai(unittest.TestCase):
    def setUp(self):
        """Prepare tests."""
        self.cube = Cube([1.0], var_name='lai', units='J')
        self.fix = Lai()

    def test_fix_data(self):
        cube = self.fix.fix_data(self.cube)
        self.assertEqual(cube.data[0], 1.0 / 100.0)
        self.assertEqual(cube.units, Unit('J'))


class TestNbp(unittest.TestCase):
    """Tests for nbp."""

    def setUp(self):
        """Prepare tests."""
        """Prepare temp folder for test."""
        self.cube = Cube([1.0], var_name='nbp')
        self.fix = Nbp()
        self.temp_folder = tempfile.mkdtemp()

    def tearDown(self):
        """Delete temp folder."""
        shutil.rmtree(self.temp_folder)

    def test_fix_file(self):
        """Test fix on nbp files to set standard_name."""
        temp_handler, temp_path = tempfile.mkstemp('.nc', dir=self.temp_folder)
        os.close(temp_handler)
        output_dir = os.path.join(self.temp_folder, 'fixed')

        iris.save(self.cube, temp_path)
        new_path = self.fix.fix_file(temp_path, output_dir)
        new_cube = iris.load_cube(new_path)
        self.assertEqual(
            new_cube.standard_name,
            'surface_net_downward_mass_flux_of_carbon_dioxide_'
            'expressed_as_carbon_due_to_all_land_processes')
