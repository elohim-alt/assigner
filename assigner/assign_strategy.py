from abc import ABC, abstractmethod
from typing import List, Tuple


class AssignStrategy(ABC):
    @abstractmethod
    def assign(self, drivers: List[str], shipments: List[str]) -> Tuple[int, List[Tuple[str, str]]]:
        pass