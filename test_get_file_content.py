import unittest
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_get_file_content(self):
        get_file_content("calculator", "lorem.txt")

    def test_main_file(self):
        response = get_file_content("calculator", "main.py")
        print(response)

    def test_pkg_calculator(self):
        response = get_file_content("calculator", "pkg/calculator.py")
        print(response)

    def test_leading_slash_filepath(self):
        response = get_file_content("calculator", "/bin/cat")
        print(response)

    def test_non_existing_file(self):
        response = get_file_content("calculator", "pkg/does_not_exist.py")
        print(response)


if __name__ == '__main__':
    unittest.main()
