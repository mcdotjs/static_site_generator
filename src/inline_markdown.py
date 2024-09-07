import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_link___my(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        extracted = extract_markdown_links(old_node.text)
        if len(extracted) < 1:
            split_nodes.append(
                TextNode(old_node.text, old_node.text_type))
        w = old_node.text
        counter = 1
        for link in extracted:
            current_limiter = f"[{link[0]}]({link[1]})"
            sections = w.split(current_limiter)
            if counter < len(extracted):
                w = sections[counter]
            split_nodes.append(TextNode(sections[0], old_node.text_type))
            split_nodes.append(TextNode(link[0], "link", link[1]))
            counter += 1
            if len(sections[1]) > 1 and isinstance(sections[1], str):
                extracted_some = extract_markdown_links(sections[1])
                if len(extracted_some) < 1:
                    split_nodes.append(TextNode(sections[1], "text"))
                    new_nodes.extend(split_nodes)
        counter = 1
        split_nodes = []
    return new_nodes


def split_nodes_imagedddddd________(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        extracted = extract_markdown_images(old_node.text)
        if len(extracted) < 1:
            split_nodes.append(
                TextNode(old_node.text, old_node.text_type, None))
        w = old_node.text
        counter = 1
        for link in extracted:
            current_limiter = f"![{link[0]}]({link[1]})"
            sections = w.split(current_limiter)
            if counter < len(extracted):
                w = sections[counter]
            counter += 1
            if len(sections[0]) > 0:
                split_nodes.append(
                    TextNode(sections[0], old_node.text_type, None))
            split_nodes.append(TextNode(link[0], "image", link[1]))
        new_nodes.extend(split_nodes)
        counter = 1
        split_nodes = []
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    # def split_nodes_delimiter__________(old_nodes, delimiter, text_type):

#     newNodes = []
#     for node in old_nodes:
#         if node.text_type != text_type_text:
#             newNodes.append(node)
#             continue
#         segments = node.text.split(delimiter)
#         newNode = []
#         for segment in range(len(segments)):
#             if segment == 1:
#                 middle = TextNode(segments[segment], text_type, None)
#                 newNode.append(middle)
#             else:
#                 other = TextNode(segments[segment], text_type_text, None)
#                 newNode.append(other)
#         newNodes.append(newNode)
#     return newNodes

# FROM BOOOT


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    "image",
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
#
#


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
