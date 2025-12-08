import csv

def find_min_bead_age(csv_path: str = "data/mollusk_bead_articles.csv") -> int:
    """
    Find the minimum 'at least' age (in thousands of years) of beads made from the mollusk species
    linked to British Museum object '2012,5015.17', as reported in 2021 Science Advances articles.
    """
    # Step 1: Find the species associated with museum object '2012,5015.17'
    # Note: The museum number contains a comma, so it gets split across columns
    # museum_number='2012' and accepted_species_name='5015.17', with the actual species in 'journal'
    species_name = None
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Handle the malformed row where museum number is split
            if row['museum_number'] == '2012' and row['accepted_species_name'] == '5015.17':
                species_name = row['journal']  # Actual species is shifted to journal column
                break
    
    if not species_name:
        raise ValueError("Museum object '2012,5015.17' not found")
    
    # Step 2: Filter rows by species, journal, and year, then find minimum age
    min_age = float('inf')
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (row['accepted_species_name'] == species_name and
                row['journal'] == 'Science Advances' and
                row['publication_year'] == '2021' and
                row['min_age_thousand_years_at_least']):
                
                age = int(row['min_age_thousand_years_at_least'])
                min_age = min(min_age, age)
    
    if min_age == float('inf'):
        raise ValueError("No matching records found")
    
    return min_age