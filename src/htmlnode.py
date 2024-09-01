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
