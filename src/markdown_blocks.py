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
