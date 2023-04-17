import unittest

from assigner.core import ShipmentAssigner


def score_ones_strategy(driver, shipment):
    return 1


def assign_in_order_strategy(drivers, shipments, score_strategy):
    # this is a very simple strategy that just assigns the first driver to the first shipment note it only makes
    # sense if same size
    assignments = [[drivers[i], shipments[i]] for i in range(len(drivers))]
    score = sum([score_strategy(driver, shipment) for driver, shipment in assignments])
    return score, assignments


class AssignInOrderStrategy:
    def __init__(self, score_strategy):
        self.score_strategy = score_strategy

    def assign(self, drivers, shipments):
        assignments = [[self.drivers[i], self.shipments[i]] for i in range(len(self.drivers))]
        total_score = sum([self.score_strategy(driver, shipment) for driver, shipment in assignments])


class AssignerTest(unittest.TestCase):
    def test_structure(self):
        drivers = ["john", "bill", "juan"]
        shipments = ["11th street", "34th street", "lincoln avenue"]

        assigner = ShipmentAssigner(drivers, shipments, AssignInOrderStrategy, score_ones_strategy)
        self.assertEqual(assigner.get_strategy_score(), 3)
        self.assertEqual(assigner.get_assignments(),
                         [["john", "11th street"], ["bill", "34th street"], ["juan", "Lincoln avenue"]])

        # def test_hungarian_with_ones_strategy(self):
    #     drivers = ["john", "bill", "juan"]
    #     shipments = ["11th street", "34th street", "lincoln avenue"]
    #
    #     assigner = ShipmentAssigner(drivers, shipments, assign_hungarian_strategy, score_ones_strategy)
    #     self.assertEqual(assigner.get_strategy_score(), 3)
    #     self.assertEqual(assigner.get_assignments(), [["john", "11th street"], ["bill", "34th street"], ["juan", "lincoln avenue"]])


if __name__ == '__main__':
    unittest.main()
