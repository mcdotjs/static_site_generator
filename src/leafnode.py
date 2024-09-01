from htmlnode import HTMLNode
# is html node without children


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leafnode was not provided with value")
        if self.tag is None:
            return f"{self.value}"
        attributes = ""
        if self.props:
            attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
