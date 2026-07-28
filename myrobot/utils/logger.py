import os
from datetime import datetime
from config.settings import LOG_FILE

LOG_PATH = "logs/robot.log"


def write_log(message):

    os.makedirs("logs", exist_ok=True)

    with open(LOG_PATH, "a", encoding="utf-8") as file:

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{time}] {message}\n")