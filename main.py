import os
import numpy as np
import json
from config import CONFIG
from loader.dataLoader import loadImg
from util.visualize import showHist, showImg
from skyDetector.predict import predictSkyRatio 

# Check path
# os.chdir(CONFIG.HOME_DIR)

# Validation of lat and long
assert len(CONFIG.LAT_LIST) == len(CONFIG.LON_LIST), "Lat size and long size are different each other"

# Load GSV images and depthmap
for idx in range(len(CONFIG.LAT_LIST)):
    lat = CONFIG.LAT_LIST[idx]
    lon = CONFIG.LON_LIST[idx]

    # Load an image from GSV API
    image, panoID = loadImg(lat, lon, CONFIG.API_KEY, CONFIG.HEADING, CONFIG.FOV)
    showImg(image)
    print(panoID)

    # # Make mask to remove sky
    # skyRatio, mask = predictSkyRatio(image)
    # showImg(mask)


