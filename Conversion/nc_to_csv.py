import xarray as xr
DS = xr.open_dataset("wrfout_d01_2024-08-25_00_00_00")
DS["T2"].to_dataframe().to_csv("output_filename.csv")