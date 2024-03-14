import requests
import sys, os
from PIL import Image
import json
import io
import numpy as np
import matplotlib.pyplot as plt
import skimage

sys.path.append(os.pardir)

def loadImg(lat, lon, APIkey, heading, fov):
    endpoint = 'https://maps.googleapis.com/maps/api/streetview/metadata'

    location = f'{lat},{lon}'
    image_container = []

    params = {
        'location': location,
        'key': APIkey,
        'heading': f"{heading}",
        'fov': f"{fov}"
    }
    url = f"https://maps.googleapis.com/maps/api/streetview?size=640x192&location={params['location']}&heading={params['heading']}&fov={params['fov']}&key={params['key']}"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    panoID = response.status_code

    bytes_data = response.content
    image = Image.open(io.BytesIO(bytes_data))

    return image, panoID

def loadLocalImg(path):
    imageOriginal = skimage.io.imread(path)
    image = skimage.transform.resize(imageOriginal, (320, 1024))
    image = image[:, :, :3]
    image = skimage.img_as_ubyte(image)
    return image