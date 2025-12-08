import pytest
from src.solution import find_nonnative_zip_codes

def test_find_nonnative_zip_codes():
    result = find_nonnative_zip_codes()
    expected = ["33040", "60601", "96701", "96706", "96734"]
    assert result == expected, f"Expected {expected}, got {result}"

def test_find_nonnative_zip_codes_with_custom_path():
    # Assuming the CSV is in the default path, but test with explicit path
    result = find_nonnative_zip_codes("data/usgs_nemo_observations.csv")
    expected = ["33040", "60601", "96701", "96706", "96734"]
    assert result == expected