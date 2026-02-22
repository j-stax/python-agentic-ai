import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_write_file_to_loremtxt(self):
        response = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(response)
    
    def test_write_file_to_pkg_moreloremtxt(self):
        response = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(response)
    
    def test_write_file_to_temp_loremtxt(self):
        response = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(response)

if __name__ == '__main__':
    unittest.main()