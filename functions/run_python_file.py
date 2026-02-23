import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        output_str = ""
        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        command = ["python", file_path_abs]
        if args:
            command.extend(args)
        
        result = subprocess.run(
            command, 
            cwd=working_directory, 
            capture_output=True, 
            text=True, 
            timeout=30
        )

        if result.returncode != 0:
            output_str += f'Process exited with code {result.returncode}\n'
        if result.stdout == None or result.stderr == None:
            output_str += "No output produced\n"
        else:
            output_str += f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'

        return output_str
    except Exception as e:
        return f'Error: executing Python file: {e}'
    

if __name__ == '__main__':
    res = run_python_file("calculator", "main.py", ["3 + 5"])
    print(res)