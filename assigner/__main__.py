import sys

from assigner.file_utils import read_as_list
from assigner.shipment_assigner import ShipmentAssigner
from assigner.scientific_score import score as scientific_score


def main(drivers_file: str, shipments_file: str):
    shipments = read_as_list(shipments_file)
    drivers = read_as_list(drivers_file)
    score, assignments = ShipmentAssigner(scientific_score).assign(drivers, shipments)

    print("Total Suitability Score: ", score)
    print("Shipment Assignments:")
    for driver, shipment in assignments:
        print(f"{driver} -> {shipment}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m assigner <drivers_file> <shipments_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
