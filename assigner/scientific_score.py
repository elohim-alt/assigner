import math


def _count_vowels(word: str) -> int:
    return sum(1 for c in word.lower() if c in "aeiou")


def _count_consonants(word: str) -> int:
    return sum(1 for c in word.lower() if c in "bcdfghjklmnpqrstvwxyz")


# We determine if the numbers have common factors by using python built in gcd.
# This internally uses the  Euclidean algorithm so complexity is O(log(min(a,b)))
def _has_common_factors(num1: int, num2: int):
    return math.gcd(num1, num2) > 1


def score(driver: str, shipment: str) -> float:
    if len(shipment) % 2 == 0:
        base_ss = _count_vowels(driver) * 1.5
    else:
        base_ss = _count_consonants(driver)
    if _has_common_factors(len(driver), len(shipment)):
        base_ss *= 1.5

    return base_ss
