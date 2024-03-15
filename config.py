import json

# Load secret data from .secret folder
with open(".secret/common.json", "r") as f:
    secretData = json.load(f)

class CONFIG:
    HOME_DIR = r"/home/ywk0524/UNET_GSV_classification"
    SAVE_DIR = r"/home/ywk0524/UNET_GSV_classification/output"

    API_KEY = secretData['API_KEY']

    HEADING = 0
    FOV = 120

    BASE_POINT_LIST = [
        [126.971526, 127.004828, 37.466354, 37.506946],
        [127.034869, 127.005000, 37.466082, 37.484473],
        [127.038131, 127.068000, 37.445369, 37.468534]
    ]

    LAT_LIST = [37.2465739]
    LON_LIST = [127.0323537]