========================================================
README: NASA FIRMS MODIS or VIIRS Fire/Hotspot Data Download
========================================================

If you requested data from multiple instruments e.g. MODIS (combined Aqua and Terra), VIIRS (S-NPP and/or NOAA-20, NOAA-21) and LANDSAT,
you will receive an email, with download link, for each data source.

This zip file will have either one, two or three naming conventions beginning with:
    DL_FIRE_M-C61_xxxx if you requested MODIS data (C61 stands for MODIS Collection 6.1), or 
    DL_FIRE_J1V-C2_xxx if you requested VIIRS 375m data from  NOAA-20(JPSS-1)
    DL_FIRE_J2V-C2_xxx if you requested VIIRS 375m data from  NOAA-21(JPSS-2)
    DL_FIRE_SV-C2_xxxx if you requested VIIRS 375m data from S-NPP
    DL_FIRE_LS_xxx if you requested LANDSAT 30m data


The xx refers to the download request id/number. The zip file contains the data
for the requested dates in your area-of-interest.

If you requested the data in shape file format you will see the following files
contained in your zip:
    fire_xx.dbf
    fire_xx.prj
    fire_xx.shp
    fire_xx.shx
    fire_xx.cpg
    Readme.txt

If you requested the data in CSV format the file name will look like this: 
    fire_.xx.csv
    Readme.txt

Depending on the date range selected you may receive 1 or 2 files containing
Near Real-Time (NRT) data and/or older standard/science quality data. NRT data
are replaced with standard quality data when they are available (approximately 3 months).

-- fire_nrt_M-C61_xx = MODIS NRT files:(MCD14DL) MODIS Active Fire and Thermal Anomalies
                    product processed by LANCE / FIRMS

-- fire_nrt_SV-C2_xx = VIIRS 375m NRT files:(VNP14IMGTDL) VIIRS Active Fire and Thermal
                    Anomalies product from S-NPP processed by LANCE / FIRMS

-- fire_nrt_J1V-C2_xx = VIIRS 375m NRT files:(VJ114IMGDL) VIIRS Active Fire and Thermal
                    Anomalies product from NOAA-20 (JPSS-1) processed by LANCE / FIRMS

-- fire_nrt_J2V-C2_xx = VIIRS 375m NRT files:(VJ214IMGDL) VIIRS Active Fire and Thermal
                    Anomalies product from NOAA-21 (JPSS-2) processed by LANCE / FIRMS

-- fire_archive_M-C61_xx = MODIS standard quality Thermal Anomalies / Fire locations 
                        processed by the University of Maryland with a 3-month
                        lag and distributed by FIRMS. These standard data (MCD14ML) 
                        replace the NRT (MCD14DL) files when available.

-- fire_archive_SV-C2_xx = VIIRS 375m standard Active Fire and Thermal Anomalies product
                        processed by the University of Maryland with a 3-month lag and
                        distributed by FIRMS. These standard data (VNP14IMGTML) replace
                        the NRT files (VNP14IMGTDL ) when available.

-- fire_nrt_LS_xx = LANDSAT 30m NRT files: LANDSAT Active Fire and Thermal
                    Anomalies product from LANDSAT


PLEASE NOTE the standard quality data is not yet available from FIRMS for NOAA-20 and NOAA-21

For a list of attribute fields for the MODIS and VIIRS data: 
  https://www.earthdata.nasa.gov/data/tools/firms/active-fire-data-attributes-modis-viirs

For the key differences between the NRT and standard products visit:  
https://www.earthdata.nasa.gov/data/tools/firms/faq and view question on 
“What are the key differences between URT/RT/NRT and standard quality fire data?”

The MODIS and VIIRS fire files are split to ensure users clearly distinguish between
these two data sources. Should you wish to combine the datasets you will still be
able to distinguish the source using the Collection / Version field.
 
Please note: If your request results in no fire points, the accompanying ZIP file
will include an empty CSV file with a header, or an empty DBF file. If you believe
that this has occurred due to an error, please contact us at support@earthdata.nasa.gov.
 
Visit the NASA FIRMS project website at:
http://earthdata.nasa.gov/firms
https://firms.modaps.eosdis.nasa.gov/ (FIRMS Global) and
https://firms.modaps.eosdis.nasa.gov/usfs US/Canada
 
========================
PROJECTION INFORMATION
========================
The MODIS and VIIRS fire/hotspot data supplied to you are in the WGS84 Geographic
projection (the "latitude/longitude projection").
 
==========
IMPORTANT
==========
For further information, please refer to the latest version of the MODIS Fire Users
Guide which can be found via the FIRMS FAQ section (https://www.earthdata.nasa.gov/data/tools/firms/faq).
 
Please note that there is MODIS data missing from several of the data sets. There is
data missing from end of June to the beginning of July in 2001, 2002 is missing some
data throughout the data set, 2007 has some missing data from mid August and data is
missing for part of 21 April 2009, and missing for 22 April 2009. There might also be
some erroneous data present in the data set.
 
Please refer to the disclaimer below.
 
==============================
DATA CITATION AND DISCLAIMER
==============================
NASA promotes the full and open sharing of all data with the research and applications
communities, private industry, academia, and the general public. Read the NASA Data and
Information Policy.
 
If you provide the LANCE / FIRMS data to a third party, we request you follow the
guidelines in the citation and replicate or provide a link to the disclaimer.
 
CITATION
Information for FIRMS can be found at the end of this page: 
https://www.earthdata.nasa.gov/engage/open-data-services-software-policies/data-use-policy
 
DISCLAIMER
LANCE is operated by the ESDIS Project. The information presented through LANCE, GIBS, Worldview, and FIRMS are 
provided “as is” and users bear all responsibility and liability for their use of data, 
and for any loss of business or profits, or for any indirect, incidental or consequential damages arising out of any use of, 
or inability to use, the data, even if NASA or ESDIS were previously advised of the possibility of such damages, 
or for any other claim by you or any other person. Due to the spatial resolution and other characteristics of these data, 
their use for tactical decision-making or informing about conditions at a local scale are not advised.
 
ESDIS makes no representations or warranties of any kind, express or implied, including implied warranties of fitness 
for a particular purpose or merchantability, or with respect to the accuracy of or the absence or the presence or defects 
or errors in data, databases of other information. The designations employed in the data do not imply 
the expression of any opinion whatsoever on the part of ESDIS concerning the legal or development status of any country, 
territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. 
For more information please contact Earthdata Support: earthdata-support@nasa.gov.