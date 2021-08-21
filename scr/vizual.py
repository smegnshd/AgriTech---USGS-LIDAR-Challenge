# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 13:36:12 2021

@author: Smegn
"""

from .data_loader import data_loader
from data_loader import DataLoader
import geopandas as gpd
import imageio
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import mapclassify as mc
import numpy as np
import laspy
import rasterio
from rasterio import mask
import folium

sys.path.append("..")
## Plot raster/tif image
# --------------------
def plot_raster(rast_data, title=''):
    """
    Plots raster tif image both in log scale(+1) and original verion
    """
    fig, (axlog, axorg) = plt.subplots(1, 2, figsize=(14,7))
    im1 = axlog.imshow(np.log1p(rast_data)) # vmin=0, vmax=2.1)
#     im2 = axorg.imshow(rast_data)

    plt.title("{}".format(title), fontdict = {'fontsize': 15})  
    plt.axis('off')
    plt.colorbar(im1, fraction=0.03)

def visualize(bounds, region):
    get_raster_terrain(bounds=bounds,region=region)
    iowa_tif = './data/tif/'+region+'.tif'
    raster_iowa = rasterio.open(iowa_tif)
    iowa_data = raster_iowa.read(1)
    count = iowa_data[iowa_data > 0].sum()
    title = 'Log scaled (+1) and No Scale Raster plots'.format(count)
    plot_raster(iowa_data, title)