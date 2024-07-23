import copernicusmarine

ds = copernicusmarine.subset(
    dataset_id="cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m",
    dataset_version="202211",
    variables=["uo", "vo"],
    minimum_longitude=-99.08172502092629,
    maximum_longitude=25.87349328264511,
    minimum_latitude=-98.42483483537943,
    maximum_latitude=100.45887275390625,
    start_datetime="2021-01-01T00:00:00",
    end_datetime="2023-12-31T00:00:00",
    minimum_depth=0.49402499198913574,
    maximum_depth=763.3331298828125,
    username='jgradone@marine.rutgers.edu',
    password='2vqqQjQPNU0z',
    output_filename = '/home/jg1200/data/CMEMS/MEAN_CMEMS_TOTAL_UV_2021_2022_2023.nc',
    force_download=True
)

