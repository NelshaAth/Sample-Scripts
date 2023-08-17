
# Author: Nelsha Athauda
# Last Updated: 7/26/2023

# Purpose: Compile NETcdf files by year for easier annual averaging


# 2015

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2015.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2015'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Number of files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)


# 2016

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2016.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2016'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Number of files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)




# 2017

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2017.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2017'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Number of files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)




# 2018

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2018.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2018'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Number of files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)




# 2019

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2019.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2019'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)




# 2020

import netCDF4 as nc
import os

directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
files = os.listdir(directory)

output_file = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Compiled_nWF_2020.nc'
with nc.Dataset(output_file, 'w', format='NETCDF4_CLASSIC') as output_nc:
	for file in files:
		if file.startswith('Surface_PM25_2020'):
			filename = os.path.join(directory, file)
			with nc.Dataset(filename) as data:
				if not hasattr(output_nc, 'lon'):
					output_nc.createDimension('lon', len(data.dimensions['lon']))
					output_nc.createVariable('lon', 'f4', ('lon',)).[:] = data.variables['lon'][:]
				if not hasattr(output_nc, 'lat'):
					output_nc.createDimension('lat', len(data.dimensions['lat']))
					output_nc.createVariable('lat', 'f4', ('lat',)).[:] = data.variables['lat'][:]
				if not hasattr(output_nc, 'PM25'):
					output_nc.createVariable('PM25', 'f4', ('lat', 'lon'))
				output_nc.variables['PM25'][:] += data.variables['PM25'][:]

print(f'Compiled NetCDF file saved to: {output_file}')
print(f'Files compiled: {len(files)}')
print('File names:')
for file in files:
	print(file)


