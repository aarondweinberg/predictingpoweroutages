# Data Sources

## Included in the competition:
- **eaglei**: https://figshare.com/articles/dataset/The_Environment_for_Analysis_of_Geo-Located_Energy_Information_s_Recorded_Electricity_Outages_2014-2022/24237376
- **NOAA Storm Events**: https://www.ncdc.noaa.gov/stormevents/


## Additional Sources:
### Energy Data
- **US Energy Information Administration US Energy Atlas**:
  - Electric retail service territories: https://atlas.eia.gov/datasets/geoplatform::electric-retail-service-territories-2/explore
  - Power plants: https://atlas.eia.gov/datasets/eia::power-plants/explore
- **American Geosciences Institute**: I’ve read that they have maps/data about energy infrastructure, but I’m having trouble finding it online (https://profession.americangeosciences.org/research)
- **US DoE City and County Energy Profiles**: Has county-level electricity consumption by sector https://catalog.data.gov/dataset/city-and-county-energy-profiles-60fbd

### Energy/Infrastructure Data We Don’t Have...
- **Power Grid by County**: North America is divided into six power grid regions (see https://www.epa.gov/green-power-markets/us-grid-regions). Seems like we’d want to know which region each county is in?
- **Buried Power Lines**: Comprehensive data don’t appear to exist; local data may be available (e.g., https://webmaps.sandiego.gov/portal/apps/Cascade/index.html?appid=929e10afa0b64837a21e49e3df343149)
- **Quality and Robustness of Energy Infrastructure**


### Weather Data
- **ERA5 Downloads**
	- **Official documentation about how to download ERA5**: https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5
	- **Download from Google** https://console.cloud.google.com/marketplace/product/bigquery-public-data/arco-era5?inv=1&invt=Abq4wg&project=master-chess-349017
    - **Download using the ecmwf package**: https://github.com/ecmwf/ecmwf-opendata
    - **Download from ECMWF**: https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5
    - **Copernicus Climate Data Store**: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview
- **Datasets used in WeatherBench 2**: https://weatherbench2.readthedocs.io/en/latest/data-guide.html
- **NWS Climate Data**: Looks like you need to click through a map to access data for each forecast office, but maybe the data can be bulk-downloaded? (https://www.weather.gov/wrh/climate)

### Topography Data
- **ERA5-Land**: Describes various features of the surface of the earth (e.g., lake depth, snow cover, leaf cover) https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land

### GIS Data
- **USGS National Map**: https://www.usgs.gov/tools/download-data-maps-national-map
- **Free GIS data**: (Includes lots of relevant-looking data sets) https://freegisdata.rtwilson.com/

### Risk-Related Data
- **NOAA emPOWER Map**: A map with information about Medicare beneficiaries who rely on electric-dependent medical and assistive equipment (https://empowerprogram.hhs.gov/empowermap)
- **NASA FIRMS**: Fire Information for Resource Management System has historical data about fires (https://firms.modaps.eosdis.nasa.gov/download/)
- **FEMA National Risk Index**: Available by county (https://hazards.fema.gov/nri/data-resources)
- ***Disaster Resilience**: Reports several resilience scores for each county (https://www.statsamerica.org/downloads/default.aspx)

### Demographic Data
- **NACo County Explorer**: The National Association of Counties has an interactive map generator with many variables; seems like the underlying data sets should be available? (https://explorer.naco.org/)
- **NWS List of Counties**: A list of counties with corresponding FIPS codes, location, etc. (https://www.weather.gov/gis/Counties)