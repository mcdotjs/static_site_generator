from htmlnode import LeafNode
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


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
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node___it_has_to_be_standalone_function____not_method(self):
        if self.text_type not in [text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image]:
            raise ValueError(f"Invalid text type: {self.text_type}")
        elif self.text_type is text_type_text:
            return LeafNode(None, self.text)
        elif self.text_type is text_type_bold:
            return LeafNode("b", self.text)
        elif self.text_type is text_type_italic:
            return LeafNode("i", self.text)
        elif self.text_type is text_type_code:
            return LeafNode("code", self.text)
        elif self.text_type is text_type_link:
            return LeafNode("a", self.text, {'href': self.url})
        elif self.text_type is text_type_image:
            return LeafNode("img", self.text, {'src': self.url, 'alt': self.text})


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
