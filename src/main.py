from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


def main():
    a = TextNode("This is a text node", "image", "https://www.google.com")
    print(a.text_node_to_html_node().__repr__())
    # attrbts = {
    #     "href": "https://www.google.com",
    #     "target": "_blank",
    # }
    # node = HTMLNode("h1", "test", [], attrbts)
    # leafnode = LeafNode("a", "Mirko attributes ?????", attrbts)
    #
    # P = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #     ],
    # )
    # print(P.to_html())


main()
