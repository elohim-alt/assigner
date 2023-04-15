import sys
from .core import assigner


def main(shipments_file, drivers_file):
    shipments = ["one", "two", "three"]
    drivers = ["john", "bill", "other"]
    best_score, best_assignments = assigner(shipments, drivers)

    print("Total Suitability Score: ", best_score)
    print("Shipment Assignments:")
    for driver, shipment in best_assignments:
        print(f"{driver} -> {shipment}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m assigner <shipments_file> <drivers_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
