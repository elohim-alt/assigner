import sys
import unittest

from hungarian_algorithm import algorithm
from munkres import Munkres, print_matrix

from assigner.shipment_assigner import ShipmentAssigner


def score_strategy_creator(score_matrix):
    def score_strategy(driver: str, shipment: str) -> float:
        return score_matrix[int(driver)][int(shipment)]

    return score_strategy


class HungarianAssignerTest(unittest.TestCase):
    """
    These tests are focus on making sure that the behavior of the assigner once we have a score matrix is correct,
    The behavior of the scores are tested on its own test file.
    """
    def test_munker_assigner_on_square_matrix(self):

        drivers = ['0', '1', '2']
        shipments = ['0', '1', '2']
        matrix = [[5, 9, 1],
                  [10, 3, 2],
                  [8, 7, 4]]
        scorer = score_strategy_creator(matrix)
        assigner = ShipmentAssigner(scorer)
        total, pairs = assigner.assign(drivers, shipments)

        wanted_pairs = [('0', '1'), ('1', '0'), ('2', '2')]
        self.assertEqual(wanted_pairs, pairs)
        self.assertEqual(23, total)

    def test_assigner_more_drivers(self):

        drivers = ['0', '1', '2', '3']
        shipments = ['0', '1', '2']
        matrix = [[5, 9, 1],
                  [10, 3, 2],
                  [8, 7, 4],
                  [1, 2, 5]]
        scorer = score_strategy_creator(matrix)
        assigner = ShipmentAssigner(scorer)
        total, pairs = assigner.assign(drivers, shipments)

        wanted_pairs = [('0', '1'), ('1', '0'), ('3', '2')]
        self.assertEqual(wanted_pairs, pairs)
        self.assertEqual(24, total)

    def test_assigner_more_shipments(self):

            drivers = ['0', '1', '2']
            shipments = ['0', '1', '2', '3']
            matrix = [[5, 9, 1, 11],
                    [10, 3, 2, 4],
                    [8, 7, 4, 5]]
            scorer = score_strategy_creator(matrix)
            assigner = ShipmentAssigner(scorer)
            total, pairs = assigner.assign(drivers, shipments)

            wanted_pairs = [('0', '3'), ('1', '0'), ('2', '1')]
            self.assertEqual(wanted_pairs, pairs)
            self.assertEqual(28, total)


if __name__ == '__main__':
    unittest.main()
