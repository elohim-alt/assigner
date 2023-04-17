import unittest
from unittest import main
from unittest.mock import patch, mock_open

from assigner import file_utils


class FileUtilsTest(unittest.TestCase):

    def test_internal_read_file_list(self):
        file_contents = "john\nbill\nother"
        with patch("builtins.open", mock_open(read_data=file_contents)) as mock_file:
            self.assertEqual(file_utils.read_as_list("tests/test_data/drivers.txt"), ["john", "bill", "other"])


if __name__ == "__main__":
    main()
