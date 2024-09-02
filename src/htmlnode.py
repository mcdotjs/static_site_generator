class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented error")

    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for item in self.props:
            result += f' {item}="{self.props[item]}"'
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


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
