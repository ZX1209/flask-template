#!/usr/bin/python3

import os
from pathlib import Path
import subprocess
import json
import time

needupdate = True

upPath = Path("./static/upside/")

picOutBase = Path("./static/covers")

filelistPath = picOutBase / "filelist.json"
# cmdlistPath = picOutBase / "cmdlist.json"

filelist = []
cmdlist = []

# load file
if filelistPath.exists():
    with open(filelistPath, "r") as fobj:
        filelist = json.load(fobj)

## should only add the new cmd
# if cmdlistPath.exists():
#     with open(cmdlistPath, "r") as fobj:
#         cmdlist = json.load(fobj)


# data gen
def gen_video_cover(rootPath):
    """gen_video_cover
    """
    global filelist, cmdlist
    for item in rootPath.iterdir():
        if item.is_dir():
            gen_video_cover(item)
        elif item.is_file() and item.suffix == ".mp4":
            print(item.name)
            if str(item) in filelist:
                pass
            else:
                filelist.append(str(item))
                cmdlist.append(
                    [
                        "ffmpeg",
                        "-ss",
                        "00:02:00.000",
                        "-y",
                        "-i",
                        str(item),
                        "-r",
                        "1",
                        "-vframes",
                        "1",
                        "-an",
                        "-vcodec",
                        "mjpeg",
                        str(picOutBase / (str(item.stem) + ".jpg")),
                    ]
                )


# gen data
if needupdate:
    gen_video_cover(upPath)

# save file
with open(filelistPath, "w") as fobj:
    json.dump(filelist, fobj)

# with open(cmdlistPath, "w") as fobj:
#     json.dump(cmdlist, fobj)

# execute cmd

processCount = 0

procs = []
for cmd in cmdlist:
    procs.append(subprocess.Popen(cmd))
    ## for memory
    # processCount += 1
    # if processCount > 100:
    #     for p in procs:
    #         p.wait()

    #     procs = []
    #     processCount = 0

for p in procs:
    p.wait()
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
