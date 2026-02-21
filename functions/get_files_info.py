import os

def get_files_info(working_directory, directory="."):
    content_details = ""

    # Ensure the working_directory is an absolute path
    working_dir_path = os.path.abspath(working_directory)

    # Construct the full path
    full_path = os.path.abspath(os.path.join(working_dir_path, directory))

    print(full_path)

    try:
        # Check if the absolute path is outside the working directory
        if not full_path.startswith(working_dir_path):
            raise ValueError(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        # Check if the directory is not a directory
        if not os.path.isdir(full_path):
            raise ValueError(f'Error: "{directory}" is not a directory')
    
    except ValueError as excpt:
        print(excpt)
        return excpt
    
    # Parse through the directory and build string of content details
    items = os.path.listdir(full_path)
    for item in items:
        item_path = os.path.join(full_path, item)



if __name__ == "__main__":
    working_dir = '.'
    relative_dir = './calculator'
    get_files_info(working_dir, relative_dir)