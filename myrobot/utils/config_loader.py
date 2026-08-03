import json


def load_config(path):
    """
    读取JSON配置文件
    """

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except FileNotFoundError:

        print("配置文件不存在")

        return []
class ConfigLoader:


    @staticmethod
    def load(path):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)