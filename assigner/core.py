from typing import List


class ShipmentAssigner:
    def __init__(self, drivers: List[str], shipments: List[str], assigner: AssignmentStrategy):
        self.total_score, self.assignments = assigner.assign(drivers, shipments)

    def get_strategy_score(self):
        return self.total_score

    def get_assignments(self):
        return self.assignments
