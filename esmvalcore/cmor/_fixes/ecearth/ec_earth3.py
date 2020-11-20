from ..fix import Fix
import cf_units


class AllVars(Fix):
    """Fixes for all vars."""

    def fix_metadata(self, cubes):
        """Fix parent time units.

        Parameters
        ----------
        cubes : iris.cube.CubeList
            Input cubes.

        Returns
        -------
        iris.cube.CubeList

        """
        for cube in cubes:
            time = cf_units.Unit(cube.coord('time').units.origin, calendar='gregorian')
            cube.coord('time').units = time
        return cubes