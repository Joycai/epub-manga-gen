class ImageTemplateLoader:
    template_content: str
    width: int
    height: int

    def build_html(self, img_name: str, landscape: bool = False) -> str:
        content = self.template_content.replace("{idcode}", img_name)
        if landscape:
            content = content.replace("{width}", str(self.height))
            content = content.replace("{height}", str(self.width))
        else:
            content = content.replace("{width}", str(self.width))
            content = content.replace("{height}", str(self.height))
        return content

    def __init__(self, file_path: str, width: int, height: int):
        with open(file_path, encoding="utf-8") as f:
            template_content = f.read()
        self.template_content = template_content
        self.width = width
        self.height = height
