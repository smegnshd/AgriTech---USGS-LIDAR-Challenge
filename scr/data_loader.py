# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:17:44 2021

@author: Smegn
"""

import logging
from url_metadata import metadata
from logger_creator import CreateLogger
import extraction, requests
from osgeo import ogr 
from osgeo import osr
import glob
import json
import shutil
import pdal
import json
import os
ogr.UseExceptions()

logger = CreateLogger('DataLoader')
logger = logger.get_default_logger()




PUBLIC_DATA_PATH="https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
default='pipeline.json'

 
class DataLoader():
    def __init__(self, data_path_access:str=PUBLIC_DATA_PATH) -> None:
        self._data_path_access = data_path_access
    def get_raster_terrain(bounds:str,region:str,default:str=default)->None:
        PUBLIC_ACCESS_PATH=PUBLIC_DATA_PATH + region + "/ept.json"
        LAZ_file='./data/laz/'+region+'.laz'
        TIF_file='./data/tif/'+region+'.tif'


        with open(default) as json_file:
            the_json= json.load(json_file)
    
        the_json['pipeline'][0]['bounds']=bounds
        the_json['pipeline'][0]['filename']=PUBLIC_ACCESS_PATH
        the_json['pipeline'][3]['filename']=LAZ_file
        the_json['pipeline'][4]['filename']=TIF_file
   
        pipeline=pdal.Pipeline(json.dumps(the_json))
    
        try:
            pipe_exec=pipeline.execute()
        except RuntimeError as er:
            print(er)
            print('Runtime error, writing 0s and moving to next bounds')
            pass
    #test
if __name__ == "__init__":
  gm = DataLoader()
  gm.run()