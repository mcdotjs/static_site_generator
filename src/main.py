from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links
)


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
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


main()
