import os
from google.genai import types

def write_file(working_directory, file_path, content):
    if file_path.startswith("/"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        file_path_abs = os.path.join(working_dir_abs_path, file_path)
        valid_file_path = os.path.commonpath([working_dir_abs_path, file_path_abs]) == working_dir_abs_path

        if not valid_file_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(file_path_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        with open(file_path_abs, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: writing to file: {e}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite content to a file located in a file path, relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the file being requested, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to place in the file",
            ),
        },
        required=["file_path", "content"],
    ),
)