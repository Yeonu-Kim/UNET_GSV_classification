import os
import numpy as np
import pandas as pd
import json
import csv
from config import CONFIG
from module.dataLoader import loadImg
from util.visualize import showHist, showImg
from skyDetector.predict import predictSkyRatio
from module.pointGenerator import pointListGen

# Check path
# os.chdir(CONFIG.HOME_DIR)

# Make lat and lon list using config
pointList = pointListGen(CONFIG.BASE_POINT_LIST)
dataLen = len(pointList)

# Make dataframe using pandas
data = {
    'lat': [],
    'lon': [],
    'sky_ratio': []
}
df = pd.DataFrame(data)

# # Load GSV images and depthmap
# for idx, point in enumerate(pointList):
#     lat = point[0]
#     lon = point[1]
#     print(f"이미지 분석 중... {idx}/{dataLen}")

#     # Load an image from GSV API
#     status, image = loadImg(lat, lon, CONFIG.API_KEY, CONFIG.HEADING, CONFIG.FOV)
#     if status == 200:
#         # showImg(image)
#         # Calculate sky ratio of the image
#         skyRatio, mask = predictSkyRatio(image)
#         print(f"천공률: {skyRatio}")
#         # Add data to pandas dataframe
#         df.loc[len(df.index)] = [lat, lon, skyRatio]
#         print(df)


# df.to_csv("./result.csv", na_rep='Unknown')


