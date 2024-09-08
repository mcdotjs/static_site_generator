from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from inline_markdown import (
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node

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

from copystatic import (copy_dirs)


def main():
    copy_dirs("./static", "./public")


main()
