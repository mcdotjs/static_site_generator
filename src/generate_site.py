import os
from markdown_blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    extact_title
)


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    print_info(dir_path_content, template_path, dest_dir_path)
    source_dirs = os.listdir(dir_path_content)
    for item in source_dirs:
        if os.path.isdir(os.path.join(dir_path_content, item)):
            generate_pages_recursively(os.path.join(
                dir_path_content, item), template_path, os.path.join(dest_dir_path, item))
        else:
            generate_page(os.path.join(
                dir_path_content, item), template_path, os.path.join(dest_dir_path, "index.html"))


def generate_page(from_path, template_path, dest_path):
    print_info(from_path, dest_path, template_path)
    file = open(from_path).read()
    template_leaded = open(template_path).read()
    content = markdown_to_html_node(file).to_html()
    title = extact_title(file)
    replaced = template_leaded.replace(
        "{{ Content }}", content).replace("{{ Title }}", title)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(replaced)


def print_info(f, t, d):
    print(f"Generating page from {f} to {t} using {d}.")
