"""Derivation of variable ``dust``."""
import iris
import iris.analysis
import iris.exceptions

from ._baseclass import DerivedVariableBase


class DerivedVariable(DerivedVariableBase):
    """Derivation of variable ``dust``.

    Uses airmass and mmrdust to get the actual mass of dust in air

    """

    @staticmethod
    def required(project):
        """Declare the variables needed for derivation."""
        required = [{'short_name': 'mmrdust'}, {'short_name': 'airmass'}]
        return required

    @staticmethod
    def calculate(cubes):
        """Compute mole fraction of CO2 at surface."""
        mmrdust = cubes.extract_cube(
            iris.Constraint(name='mass_fraction_of_dust_dry_aerosol_particles_in_air'))
        airmass = cubes.extract_cube(
            iris.Constraint(name='atmosphere_mass_of_air_per_unit_area'))

        dust = mmrdust.copy(airmass.core_data() * mmrdust.core_data())
        dim_coord = dust.coord(
            axis='z',
            dim_coords=True
        )
        dust = dust.collapsed(
            dim_coord,
            iris.analysis.SUM
        )
        dust.units = 'kg m-2'
        return dust
