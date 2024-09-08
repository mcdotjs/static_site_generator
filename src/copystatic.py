import os
import shutil


def copy_dirs(source, destination):
    if destination == "./public":
        for item in os.listdir(destination):
            item_path = os.path.join(destination, item)
            # If the item is a directory, remove it and its contents
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            # If the item is a file, remove it
            elif os.path.isfile(item_path) or os.path.islink(item_path):
                if item_path != "./public/.gitignore":
                    os.remove(item_path)
    else:
        os.mkdir(destination)
    source_dirs = os.listdir(source)
    if len(source_dirs) > 0:
        for item in source_dirs:
            if os.path.isdir(os.path.join(source, item)):
                copy_dirs(os.path.join(source, item),
                          os.path.join(destination, item))
            else:
                shutil.copy(os.path.join(source, item),
                            os.path.join(destination, item))

# boot


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
