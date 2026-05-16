import os
import time
import netCDF4 as nc

class NcFile:
    def __init__(self, full_path, title, description = '', references ='', format_file="NETCDF4"):
        """
        Initializes the NcFile object by creating a NetCDF file.
        """

        directory = os.path.dirname(full_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        self.filepath = full_path
        self.ffile = format_file
        
        # Remove existing file to avoid permission errors
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        
        ncfile = nc.Dataset(self.filepath, 'w', self.ffile)

        # Attributes
        ncfile.history = "Created at " + time.ctime(time.time())
        ncfile.title = title
        ncfile.source = "Numerica Library (git@github.com:nramirez-f/numerica.git)"
        ncfile.author = "Nramirez"

        if description:
            ncfile.description = description
        if references:
            ncfile.references = references

        ncfile.close()

    def addCoords(self, spatialCoords, iterName='time', iterUnit = 's'):

        ncfile = nc.Dataset(self.filepath, 'a', self.ffile)
        
        ncfile.createDimension(iterName, None)
        ncfile.createVariable(iterName, "f8", (iterName,)).units = iterUnit

        self.coords_names = []
        for coord_name, coord_values in spatialCoords.items():
            ncfile.createDimension(coord_name, len(coord_values))
            coord_var = ncfile.createVariable(coord_name, "f8", (coord_name,))
            coord_var[:] = coord_values
            coord_var.unit = "unit"
            self.coords_names.append(coord_name)

        ncfile.close()

    def addVars(self, vars):
        
        ncfile = nc.Dataset(self.filepath, 'a', self.ffile)

        for var_name in vars:
            var = ncfile.createVariable(var_name, "f8", ('time', *self.coords_names))
            var.units = "unit"

        ncfile.close()


    def save(self, current_time, vars):
        """
        Save simulation variables for the current iteration.

        Parameters:
        - current_time: Current time of the simulation (float).
        - vars: Dictionary {variable_name: numpy_array}.
        """
        ncfile = nc.Dataset(self.filepath, 'a', format="NETCDF4")

        time_dim = len(ncfile.variables['time'])
        ncfile.variables['time'][time_dim] = current_time

        for var_name, var_values in vars.items():
            if var_name in ncfile.variables:
                ncfile.variables[var_name][time_dim, ...] = var_values
            else:
                raise ValueError(f"Variable '{var_name}' not found in the NetCDF file.")
            
        ncfile.close()