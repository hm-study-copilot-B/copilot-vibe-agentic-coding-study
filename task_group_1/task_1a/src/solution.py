from typing import List

def find_nonnative_zip_codes(csv_path: str = "data/usgs_nemo_observations.csv") -> List[str]:
    """
    Return unique 5-digit ZIP codes where the Nemo fish (clownfish) was observed as nonnative by USGS before 2020.
    Filter: data_source == "USGS", observation_year < 2020, species contains "clownfish" (case-insensitive).
    Return sorted list of strings.
    """
    ...