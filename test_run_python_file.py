import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_run_main_file(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_run_main_file_with_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_run_main_file_with_relative_path(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_run_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
    
    def test_run_lorem_text_file(self):
        result = run_python_file("calculator", "lorem.txt")
        print(result)

if __name__ == "__main__":
    unittest.main()