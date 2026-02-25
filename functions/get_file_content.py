import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    if file_path.startswith("/"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs_path, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs_path, file_path_abs]) == working_dir_abs_path
        content = ""

        # Check file_path is outside working_directory
        if not valid_file_path:
            print("Error: file path")
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check file_path leads to an actual file
        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        f = open(file_path_abs)
        content += f.read(MAX_CHARS)

        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        f.close()   

        return content
    except Exception as e:
        print(e)
        return f'Error: reading from file: {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)

if __name__ == "__main__":
    get_file_content('calculator', 'calculator/calculator.py')    