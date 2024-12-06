import xarray as xr

ds = xr.open_dataset("wrf_2km_mad_fcst_20230729.nc")

lats = ds["XLAT"].values
lons = ds["XLONG"].values

lat_min, lat_max = lats.min(), lats.max()
lon_min, lon_max = lons.min(), lons.max()

print(f"ulx: {lon_min}")
print(f"uly: {lat_max}")
print(f"lrx: {lon_max}")
print(f"lry: {lat_min}")