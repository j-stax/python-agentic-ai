import os

def get_files_info(working_directory, directory="."):
    if directory.startswith("/"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    try:
        # Use os.path.abspath() to get the absolute path of the working_directory. 
        # For example, if you pass in "calculator" as the working_directory, 
        # this might return something like "/home/steve/ai-agent-project/calculator".
        working_dir_abs_path = os.path.abspath(working_directory)

        # Construct the full path to the target directory by calling os.path.join() with 
        # the absolute working_directory and the directory argument. To protect against shenanigans, 
        # also make sure to call os.path.normpath() on the combined path. This will handle things like "..", 
        # turning the path into its true form.
        target_dir = os.path.normpath(os.path.join(working_dir_abs_path, directory))

        # Now check if target_dir falls within the absolute working_directory path. 
        # The safest way of doing this is to use os.path.commonpath(), which finds the longest sub-path shared by two paths. 
        # For example, if the working directory is "/home/steve/ai-agent-project/calculator" and 
        # the target directory is "/home/steve/ai-agent-project/calculator/pkg", 
        # then the common path will be "/home/steve/ai-agent-project/calculator". 
        # That is, the common path should be the same as the absolute working directory path – 
        # if the target directory is valid.
        valid_target_dir = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        # Check if directory arg is an actual directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        dir_items = [f for f in os.listdir(target_dir) if f != "__pycache__"]
        for item in dir_items:
            item_path = os.path.join(target_dir, item)
            print(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
    except Exception as e:
        print(f'Error: retrieving file info: {e}')


if __name__ == "__main__":
    working_dir = '.'
    relative_dir = 'calculator'
    get_files_info(working_dir, relative_dir)

