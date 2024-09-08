import os
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    extact_title
)


def generate_page(from_path, template_path, dest_path):
    print_info(from_path, dest_path, template_path)
    file = open(from_path).read()
    template_leaded = open(template_path).read()
    content = markdown_to_html_node(file).to_html()
    title = extact_title(file)
    replaced = template_leaded.replace(
        "{{ Content }}", content).replace("{{ Title }}", title)
    open(dest_path, "w").write(replaced)


def print_info(f, t, d):
    print(f"Generating page from {f} to {t} using {d}.")
