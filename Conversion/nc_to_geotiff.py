import xarray as xr
import rioxarray as rio

ds = xr.open_dataset("wrf_2km_mad_fcst_20230729.nc")
t2 = ds['T2']
t2 = t2.rio.set_spatial_dims(x_dim="west_east", y_dim="south_north")
t2 = t2.rio.write_crs("EPSG:4326", inplace=True)
t2.rio.to_raster(f"t2arm.tif")
