from typing import Callable,List, Tuple

from munkres import Munkres

# in order to have a score higher than this, driver name should have a few thousand letters
MAX_PAIR_SCORE = 10000


class ShipmentAssigner:
    """ShipmentAssigner is a class that assigns drivers to shipments using the Hungarian/Munkres algorithm."""

    def __init__(self, score_strategy: Callable[[str, str], int]):
        self.score_strategy = score_strategy

    def assign(self, drivers: List[str], shipments: List[str]) -> Tuple[int, List[Tuple[str, str]]]:
        """Assigns drivers to shipments using the Hungarian/Munkres algorithm.
        if we have more drivers than shipments, some drivers won't get shipments assigned to them.
        if we have more shipments than drivers, some shipments won't get drivers assigned to them.

        Args:
            drivers: A list of driver names.
            shipments: A list of shipments receiver streets.

        Returns:
            A tuple of the total score and a list of assignments.
        """

        matrix = [[self.score_strategy(driver, shipment) for shipment in shipments] for driver in drivers]
        cost_matrix = self._prepare_matrix(matrix)

        m = Munkres()
        indexes = m.compute(cost_matrix)
        assignments, total = self._build_pairs(drivers, shipments, indexes, matrix)

        return total, assignments

    def _build_pairs(self, drivers: List[str], shipments: List[str], indexes: List[Tuple[int, int]], matrix: List[List[int]]) -> Tuple[List[Tuple[str, str]], int]:
        total = 0
        assignments = []
        for row, column in indexes:
            value = matrix[row][column]
            total += value
            assignments += [(drivers[row], shipments[column])]
        return assignments, total

    # The library that we use just calculates the minimum cost,
    # we need to invert the scores to get the maximum profit (score)
    def _prepare_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        cost_matrix = []
        for row in matrix:
            cost_row = []
            for col in row:
                cost_row += [MAX_PAIR_SCORE - col]
            cost_matrix += [cost_row]
        return cost_matrix
