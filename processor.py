"""

"""
import os.path

from loader import ImageTemplateLoader
from utility import conv, clean_work_dir

out_dir = "dist"

if __name__ == '__main__':
    width = 768
    height = 1024
    loader = ImageTemplateLoader(os.path.join("resources", "template", "image.xhtml"), width, height)
    # conv_landscape(1, 1, loader)
    clean_work_dir(os.path.join("dist","pages"))
    conv(2, 178, loader)
    # conv_landscape(67, 67, loader)
    # conv(68, 100, loader)
    print("fin..")
