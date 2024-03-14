import json

# Load secret data from .secret folder
with open(".secret/common.json", "r") as f:
    secretData = json.load(f)

class CONFIG:
    HOME_DIR = r"/home/ywk0524/GSV-cloudpoints-generator"
    SAVE_DIR = r"/home/ywk0524/GSV-cloudpoints-generator/output"

    API_KEY = secretData['API_KEY']

    HEADING = 0
    FOV = 120

    LAT_LIST = [37.2465739]
    LON_LIST = [127.0323537]