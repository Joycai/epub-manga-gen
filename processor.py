"""

"""
import os.path

from loader import ImageTemplateLoader
from utility import conv, conv_landscape

out_dir = "dist"

if __name__ == '__main__':
    width = 1200
    height = 1600
    loader = ImageTemplateLoader(os.path.join("resources", "template", "image.xhtml"), width, height)
    # conv_landscape(1, 1, loader)
    conv(1, 29, loader)
    # conv_landscape(67, 67, loader)
    # conv(68, 100, loader)
    print("fin..")
