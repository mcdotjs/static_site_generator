from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


def main():
    a = TextNode("AAAAAAAAAAAAAAAA `text` BBBBBBBBBBBB", "text")
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
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node, a], "`", "code")
    print(new_nodes)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for node in old_nodes:
        segments = node.text.split(delimiter)
        newNode = []
        for segment in range(len(segments)):
            if segment == 1:
                middle = TextNode(segments[segment], text_type, None)
                newNode.append(middle)
            else:
                other = TextNode(segments[segment], "text", None)
                newNode.append(other)
        newNodes.append(newNode)
    return newNodes


main()
