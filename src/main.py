from textnode import TextNode
from htmlnode import HTMLnode


def main():
    a = TextNode("This is a text node", "bold", "https: // www.boot.dev")
    attrbts = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    node = HTMLnode("h1", "test", [], attrbts)
    print(node.__repr__())
    print(node.props_to_html())


main()
