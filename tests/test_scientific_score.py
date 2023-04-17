import unittest

from assigner.scientific_score import score


class ScientificScoreTest(unittest.TestCase):
    def test_destination_even_no_common_factors(self):
        got = score("don", "1st street")
        # number of vowels in juan is 1
        # street name has length 10 (even) base suitability score is 1 * 1.5 = 1.5
        # 3 and 10 have no common factors other than 1 the suitability score is equal to the base score of 1.5
        want = 1.5
        self.assertEqual(want, got)

    def test_destination_odd_no_common_factors(self):
        got = score("don", "42nd street")
        # number of consonants in don is 2
        # street name has length 11 (odd) base suitability score is 2
        # 3 and 11 have no common factors other than 1 the suitability score is equal to the base score of 2
        want = 2
        self.assertEqual(want, got)

    def test_destination_even_common_factors(self):
        got = score("juan", "1st street")
        # number of vowels in juan is 2
        # street name has length 10 (even) base suitability score is 2 * 1.5 = 3
        # 4 and 10 have common factors other than 1 the suitability score is equal to 3 * 1.5 = 4.5
        want = 4.5
        self.assertEqual(want, got)

    def test_destination_odd_common_factors(self):
        got = score("don", "42 street")
        # number of consonants in don is 2
        # street name has length 9 (odd) base suitability score is 2
        # 3 and 9 have common factors other than 1 the suitability score is equal to 2 * 1.5 = 3
        want = 3
        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
