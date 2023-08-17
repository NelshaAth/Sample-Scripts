
# Author: Nelsha Athauda
# Last Updated: 8/17/2023

# Purpose: Visualize modeled PM 2.5 data for the state of Alaska by state, borough, and with community coordinates

# Full state View PM 2.5 Map

import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import numpy as np
import xarray as xr
import cartopy.io.shapereader as shpreader
import shapely.vectorized

new_directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
os.chdir(new_directory)
os.getcwd()

# Pull NetCDF file data 
filename = 'Surface_PM25_201507_Nested_Corrected.nc'
data = nc.Dataset(filename)
pm25_variable = data['PM25'] 
pm25_values = pm25_variable[:]
lon = data['lon'][:]
lat = data['lat'][:]
data.close()

# Calculate the min and max PM2.5 values
pm25_min = pm25_values.min()
pm25_max = pm25_values.max()

# Create a plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
pcm = plt.pcolormesh(lon, lat, pm25_values[11, 0, :, :], cmap='Reds', transform=ccrs.PlateCarree(), vmin=pm25_min, vmax=pm25_max) # = Day + 1

# Add borough borders
reader = shpreader.Reader('AK_Boroughs_divided.shp')
boroughs = list(reader.geometries())
BOROUGHS = cfeature.ShapelyFeature(boroughs, ccrs.PlateCarree())

# Add coastlines and country borders
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(BOROUGHS, facecolor='none', edgecolor='black')

# Add ocean space
ocean_feature = cfeature.NaturalEarthFeature('physical', 'ocean', '50m', facecolor='lightcyan')
ax.add_feature(ocean_feature)

# Add Dates to title
date = filename.split('_')[-3].split('.')[0]
day = 12
month = date[4:6]
year = date[0:4]

# Plot extent based on data coordinates
ax.set_extent([-172.5, -140.5, 47.5, 77.5], crs=ccrs.PlateCarree()) 

# Add colorbar
cax = fig.add_axes([0.25, 0.1, 0.5, 0.02])  # Adjust the position and size of the color bar
cbar = fig.colorbar(pcm, cax=cax, orientation='horizontal')
cbar.set_label('PM2.5 (µg/m³)')

# Save plot
plt.title('PM2.5 Concentration')
ax.text(0.5, 1.05, f'Date: {month}-{day}-{year}', transform=ax.transAxes, ha='center', va='bottom', fontsize=12)
save_path = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Output/FullStateView.png' 
plt.savefig(save_path, dpi=300)



##### Map with labeled boroughs in default grid

import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import numpy as np
import xarray as xr
import cartopy.io.shapereader as shpreader
import shapely.vectorized
import shapefile
from shapely.geometry import shape


new_directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
os.chdir(new_directory)
os.getcwd()

shapefile_path = '/GIS/AK_Boroughs_divided.shp'
sf = shapefile.Reader(shapefile_path)
shapes = sf.shapes()
records = sf.records()

for i in range(len(shapes)):
	county_shape = shape(shapes[i])
	county_record = records[i]
	county_name = county_record['CommunityN']  # Field name in dbf of shapefile
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
	filename = 'Surface_PM25_201507_Nested_Corrected.nc'
	data = nc.Dataset(filename)
	pm25_variable = data['PM25']
	pm25_values = pm25_variable[:]
	lon = data['lon'][:]
	lat = data['lat'][:]
	data.close()
	pm25_min = pm25_values.min()
	pm25_max = pm25_values.max()
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
	pcm = plt.pcolormesh(lon, lat, pm25_values[11, 0, :, :], cmap='Reds', transform=ccrs.PlateCarree(), vmin=pm25_min, vmax=pm25_max) # = Day + 1
	date = filename.split('_')[-3].split('.')[0]
	day = 12
	month = date[4:6]
	year = date[0:4]
	cax = fig.add_axes([0.25, 0.1, 0.5, 0.02])
	cbar = fig.colorbar(pcm, cax=cax, orientation='horizontal')
	cbar.set_label('PM2.5 (µg/m³)')
	plt.title('PM2.5 Concentration')
	ocean_feature = cfeature.NaturalEarthFeature('physical', 'ocean', '50m', facecolor='lightcyan')
	ax.add_feature(ocean_feature)
	county_feature = cfeature.ShapelyFeature([county_shape], ccrs.PlateCarree())
	ax.add_feature(county_feature, edgecolor='black', facecolor='none')
	ax.coastlines()
	ax.add_feature(cfeature.BORDERS)
	ax.set_extent(county_shape.bounds, crs=ccrs.PlateCarree())
	xmin, ymin, xmax, ymax = county_shape.bounds
	padding = 1.0
	ax.set_extent([xmin - padding, xmax + padding, ymin - padding, ymax + padding], crs=ccrs.PlateCarree())
	pcm = ax.pcolormesh(lon, lat, pm25_values[11, 0, :, :], cmap='Reds', transform=ccrs.PlateCarree())
	label_x = (xmin + xmax) / 2
	label_y = (ymin + ymax) / 2
	ax.annotate(
		county_name,
		xy=(label_x, label_y),
		xytext=(0, 0),
		textcoords='offset points',
		ha='center',
		va='center',
		color='black',
		bbox=dict(boxstyle='square,pad=0.3', fc='white', ec='black')
	)
	plt.title(f'PM2.5 Concentration in {county_name}')
	ax.text(0.5, 1.05, f'Date: {month}-{day}-{year}', transform=ax.transAxes, ha='center', va='bottom', fontsize=12)
	save_path = f'/Modeled_Data_Analysis/Output/Samplewboroughlines_{county_name}.png'
	plt.savefig(save_path, dpi=300)
	plt.close(fig) 




## Map with labeled boroughs in default grid and layer of community coordinates

import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import numpy as np
import xarray as xr
import cartopy.io.shapereader as shpreader
import shapely.vectorized
import shapefile
from shapely.geometry import shape


new_directory = '/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Data'
os.chdir(new_directory)
os.getcwd()

city_shapefile_path = '/Modeled_Data_Analysis/GIS/AK_Comms_Updated.shp'
city_sf = shpreader.Reader(city_shapefile_path)

shapefile_path = '/Modeled_Data_Analysis/GIS/AK_Boroughs_divided.shp'
sf = shapefile.Reader(shapefile_path)
shapes = sf.shapes()
records = sf.records()

for i in range(len(shapes)):
	county_shape = shape(shapes[i])
	county_record = records[i]
	county_name = county_record['CommunityN']  # Field name in dbf of shapefile
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
	filename = 'Surface_PM25_201507_Nested_Corrected.nc'
	data = nc.Dataset(filename)
	pm25_variable = data['PM25']
	pm25_values = pm25_variable[:]
	lon = data['lon'][:]
	lat = data['lat'][:]
	data.close()
	pm25_min = pm25_values.min()
	pm25_max = pm25_values.max()
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
	pcm = plt.pcolormesh(lon, lat, pm25_values[11, 0, :, :], cmap='Reds', transform=ccrs.PlateCarree(), vmin=pm25_min, vmax=pm25_max) # = Day + 1
	date = filename.split('_')[-3].split('.')[0]
	day = 12
	month = date[4:6]
	year = date[0:4]
	cax = fig.add_axes([0.25, 0.1, 0.5, 0.02])
	cbar = fig.colorbar(pcm, cax=cax, orientation='horizontal')
	cbar.set_label('PM2.5 (µg/m³)')
	plt.title('PM2.5 Concentration')
	ocean_feature = cfeature.NaturalEarthFeature('physical', 'ocean', '50m', facecolor='lightcyan')
	ax.add_feature(ocean_feature)
	county_feature = cfeature.ShapelyFeature([county_shape], ccrs.PlateCarree())
	ax.add_feature(county_feature, edgecolor='black', facecolor='none')
	ax.coastlines()
	ax.add_feature(cfeature.BORDERS)
	ax.set_extent(county_shape.bounds, crs=ccrs.PlateCarree())
	xmin, ymin, xmax, ymax = county_shape.bounds
	padding = 1.0
	ax.set_extent([xmin - padding, xmax + padding, ymin - padding, ymax + padding], crs=ccrs.PlateCarree())
	pcm = ax.pcolormesh(lon, lat, pm25_values[11, 0, :, :], cmap='Reds', transform=ccrs.PlateCarree())
	label_x = (xmin + xmax) / 2
	label_y = (ymin + ymax) / 2
	ax.annotate(
		county_name,
		xy=(label_x, label_y),
		xytext=(0, 0),
		textcoords='offset points',
		ha='center',
		va='center',
		color='black',
		bbox=dict(boxstyle='square,pad=0.3', fc='white', ec='black')
	)
	for city_feature in city_sf:
		city_shape = city_feature.geometry
		city_lon, city_lat = city_shape.x, city_shape.y  # Access the x (lon) and y (lat) attributes of the Point
		ax.scatter(city_lon, city_lat, color='blue', s=50, transform=ccrs.PlateCarree())
	plt.title(f'PM2.5 Concentration in {county_name}')
	ax.text(0.5, 1.05, f'Date: {month}-{day}-{year}', transform=ax.transAxes, ha='center', va='bottom', fontsize=12)
	save_path = f'/mnt/c/Users/nrathauda/OneDrive - University of Alaska/NIMHD K01 - wildfire and birth outcomes/Modeled_Data_Analysis/Output/MapsAKcommunities_{county_name}.png'
	plt.savefig(save_path, dpi=300)
	plt.close(fig) 

