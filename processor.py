"""

"""
import os.path

from loader import ImageTemplateLoader
from utility import conv

out_dir = "dist"

if __name__ == '__main__':
    width = 1500
    height = 2000
    loader = ImageTemplateLoader(os.path.join("resources", "template", "image.xhtml"), width, height)
    conv(0, 10, loader)
    print("fin..")
