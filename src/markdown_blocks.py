import re
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def block_to_block_type2(block):
    lines = block.split("\n")
    if bool(re.match("^#{1,6} ", block)):
        return "heading"
    # elif bool(re.match("^```.*\n?```$", block)):
    #     return "cod
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    elif bool(re.match("^(>.*\n?)+$", block)):
        return "quote"
    elif bool(re.match("^([*-] .*\n?)+$", block)):
        return "unordered_list"
    elif bool(re.match("^(d+. .*\n?)+$", block)):
        return "ordered_list"
    else:
        return "paragraph"


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
# spliting line by line


def markdown_to_blocks2(markdown):
    lines = markdown.split("\n")
    arr = []
    block = ""
    for line in lines:
        print(line)
        if len(line) == 0:
            print("0", line)
            if len(block) > 0:
                arr.append(block)
            block = ""
        else:
            print("else", line)
            block += line.strip() + "\n"
    if len(block) > 0:
        arr.append(block)
    return arr

# spliting right to blocks


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        print("oOOOOO", block)
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
