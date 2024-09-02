from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode


def main():
    a = TextNode("This is a text node", "bold", "https: // www.boot.dev")
    attrbts = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    node = HTMLNode("h1", "test", [], attrbts)
    leafnode = LeafNode("a", "Mirko attributes ?????", attrbts)
    print(leafnode.to_html())


main()
