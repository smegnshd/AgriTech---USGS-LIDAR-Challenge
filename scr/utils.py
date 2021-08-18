import geopandas as gpd
import numpy as np
from shapely.geometry import Polygon
  
def local_max(MINX, MINY, MAXX, MAXY):
    polygon = Polygon(((MINX, MINY), (MINX, MAXY), (MAXX, MAXY), (MAXX, MINY), (MINX, MINY)))
    grid = gpd.GeoDataFrame([polygon], columns=["geometry"])
    grid.set_crs(epsg=4326, inplace=True)
    return polygon,grid 
 
 
local_max(-93.756155, 41.918015, -93.747334, 41.921429)
  