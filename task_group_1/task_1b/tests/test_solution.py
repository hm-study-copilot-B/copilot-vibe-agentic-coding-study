import pytest
from src.solution import find_min_bead_age

def test_find_min_bead_age():
    result = find_min_bead_age()
    expected = 90
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_min_bead_age_with_custom_path():
    result = find_min_bead_age("data/mollusk_bead_articles.csv")
    expected = 90
    assert result == expected