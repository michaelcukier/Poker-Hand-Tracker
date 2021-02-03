import unittest

from helpers.extract_id_from_title import extract_id_from_title
from fake_data_tourneys.fake_data import examples_titles_id_extraction


class test_dict_to_clean_data(unittest.TestCase):
    def test_extract_id_from_title(self):
        self.assertEqual(
            extract_id_from_title(examples_titles_id_extraction[1]),
            '23231703')
        self.assertEqual(
            extract_id_from_title(examples_titles_id_extraction[0]),
            '23231703')


if __name__ == '__main__':
    unittest.main()

