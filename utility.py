import os
import shutil

from loader import ImageTemplateLoader

target_dir = os.path.join("dist", "pages")

def clean_work_dir(path:str):
    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))


def build_id(i: int, length: int = 3) -> str:
    prefix = ""
    if len(str(i)) < length:
        to_append = length - len(str(i))
        for itr in range(0, to_append):
            prefix = prefix + "0"
    return prefix + str(i)


def write_file(file_name: str, content: str):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(os.path.join(target_dir, file_name), "w", encoding="utf-8") as f:
        f.write(content)


def conv_landscape(start: int, end: int, template_loader: ImageTemplateLoader):
    for i in range(start, end + 1):
        file_idx = build_id(i)
        content = template_loader.build_html(file_idx, True)
        write_file('Section%s.xhtml' % file_idx, content)


def conv(start: int, end: int, template_loader: ImageTemplateLoader):
    for i in range(start, end + 1):
        file_idx = build_id(i)
        content = template_loader.build_html(file_idx)
        write_file('Section%s.xhtml' % file_idx, content)
