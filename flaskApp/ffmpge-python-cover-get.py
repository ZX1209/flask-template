#!/usr/bin/python3

import os
from pathlib import Path
import subprocess


upPath = Path("./static/upside/")

picOutBase = Path("./static/covers")


def gen_video_cover(rootPath):
    """gen_video_cover
    """
    for item in rootPath.iterdir():
        if item.is_dir():
            gen_video_cover(item)
        elif item.is_file() and item.suffix == ".mp4":
            print(item.name)
            subprocess.call(
                [
                    "ffmpeg",
                    "-y",
                    "-i",
                    item,
                    "-ss",
                    "00:01:00.000",
                    "-vframes",
                    "1",
                    picOutBase / (str(item.stem) + ".jpg"),
                ]
            )


gen_video_cover(upPath)
# for (dirpath, dirnames, filenames) in os.walk(upPath):
#     if item.suffix == ".mp4":
#         subprocess.call(
#             [
#                 "ffmpeg",
#                 "-y",
#                 "-i",
#                 item,
#                 "-ss",
#                 "00:00:05.000",
#                 "-vframes",
#                 "1",
#                 picOutBase / item.name,
#             ]
#         )
