class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, another):
        t = self.text == another.text
        t_type = self.text_type == another.text_type
        u = self.url == another.url
        if t and t_type and u:
            return True

    def __repr__(self):
        return print(f"TextNode({self.text}, {self.text_type}, {self.url})")
