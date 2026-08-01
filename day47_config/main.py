import json
from camera import Camera


with open(
    "config.json",
    "r",
    encoding="utf-8"
) as f:

    config=json.load(f)



camera=Camera(
    config["camera"]
)


camera.show()