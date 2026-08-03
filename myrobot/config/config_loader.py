import json

import os
print(os.getcwd())
class ConfigLoader:

    @staticmethod
    def load():

        with open(
            "config/robot_config.json",
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)