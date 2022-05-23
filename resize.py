import os
import re
from typing import Callable, Union

from utility import write_file

xhtml_path = ""


def process_xhtml(file_name: str, file_path: str):
    print(file_name)
    width = "1024"
    height = "768"
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
        # viewport
        reobj = re.compile("content=\"width=[0-9]+, height=[0-9]+\"")
        result, number = reobj.subn("content=\"width=%s, height=%s\"" % (width, height), content)
        # view box
        vbobj = re.compile("viewBox=\"0 0 [0-9]+ [0-9]+\"")
        result, number = vbobj.subn("viewBox=\"0 0 %s %s\"" % (width, height), result)
        # image
        imgbj = re.compile("width=\"[0-9]+\" height=\"[0-9]+\"")
        result, number = imgbj.subn("width=\"%s\" height=\"%s\"" % (width, height), result)

    write_file(file_path, result)


def process_file(path, func: Callable[[str, str], Union[None, bool]]):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith("Section"):
                func(file, os.path.join(root, file))


if __name__ == '__main__':
    process_file(xhtml_path, process_xhtml)
