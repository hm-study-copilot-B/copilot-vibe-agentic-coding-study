import csv
from typing import List

def find_nonnative_zip_codes(csv_path: str = "data/usgs_nemo_observations.csv") -> List[str]:
    """
    Return unique 5-digit ZIP codes where the Nemo fish (clownfish) was observed as nonnative by USGS before 2020.
    Filter: data_source == "USGS", observation_year < 2020, species contains "clownfish" (case-insensitive).
    Return sorted list of strings.
    """
    zip_codes = set()
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Filter conditions
            if (row['data_source'] == 'USGS' and
                int(row['observation_year']) < 2020 and
                'clownfish' in row['species_common_name'].lower()):
                
                # Extract ZIP code and add to set
                zip_code = row['zip_code'].strip()
                if len(zip_code) == 5 and zip_code.isdigit():
                    zip_codes.add(zip_code)
    
    # Return sorted list
    return sorted(list(zip_codes))