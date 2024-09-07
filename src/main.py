from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from inline_markdown import (
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)
from markdown_blocks import (
    markdown_to_blocks
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)


def main():
    a = TextNode("AAAAAAAAAAAAAAAA", "text")
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
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "text"
    )

    node1 = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "text"
    )

    node2 = TextNode(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        text_type_text,
    )

    nodeI = TextNode(
        "![image](https://www.example.com/image.png)",
        text_type_text,
    )
    t = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    m = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
    new_nodes = markdown_to_blocks(m)
    print(new_nodes)


main()
