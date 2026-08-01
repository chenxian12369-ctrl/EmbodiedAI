def write_log(message):

    with open(
        "robot.log",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(message+"\n")