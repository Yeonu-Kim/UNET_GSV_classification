import requests
import sys, os
from PIL import Image
import json
import io
import numpy as np
import matplotlib.pyplot as plt
import skimage

sys.path.append(os.pardir)

def loadImg(lat:float, lon:float, APIkey:str, heading:int, fov:int):
    endpoint = 'https://maps.googleapis.com/maps/api/streetview/metadata'

    params = {
        'location': f"{lon},{lat}",
        'key': APIkey,
        'heading': f"{heading}",
        'fov': f"{fov}"
    }
    url = f"https://maps.googleapis.com/maps/api/streetview?size=640x192&location={params['location']}&heading={params['heading']}&fov={params['fov']}&return_error_code=true&key={params['key']}"

    response = requests.get(url)
    status = response.status_code

    bytes_data = response.content
    image = Image.open(io.BytesIO(bytes_data)) if status == 200 else None
    return status, image

def loadLocalImg(path:str):
    imageOriginal = skimage.io.imread(path)
    image = skimage.transform.resize(imageOriginal, (320, 1024))
    image = image[:, :, :3]
    image = skimage.img_as_ubyte(image)
    return image