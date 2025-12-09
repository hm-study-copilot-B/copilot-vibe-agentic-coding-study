"""
CSV Parser with Command Support
BUGGY IMPLEMENTATION - Commands are case-sensitive but should not be!
"""


def parse_csv_with_commands(data):
    """
    Parse a CSV file that may contain special command lines.
    
    Command lines start with '#' and control parsing behavior:
    - #SKIP N: Skip N data rows
    - #DELIMITER <char>: Set delimiter (comma, tab, space, semicolon)
    - #COMMENT <char>: Set comment character
    
    BUG: Currently only recognizes UPPERCASE commands, but should be case-insensitive.
    
    Parameters:
    - data: String containing CSV data with optional command lines
    
    Returns:
    - Dictionary with keys: 'rows' (list of data rows), 'skip', 'delimiter', 'comment_char'
    """
    lines = data.strip().split('\n')
    
    skip_rows = 0
    delimiter = ','
    comment_char = None
    rows = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # BUG: Commands are checked with exact case matching
        # Should convert to uppercase for case-insensitive comparison
        if line.startswith('#SKIP'):
            # Parse skip command: #SKIP 2
            parts = line.split()
            if len(parts) >= 2:
                skip_rows = int(parts[1])
                
        elif line.startswith('#DELIMITER'):
            # Parse delimiter command: #DELIMITER tab
            parts = line.split(maxsplit=1)
            if len(parts) >= 2:
                delim_name = parts[1].strip()
                if delim_name == 'tab':
                    delimiter = '\t'
                elif delim_name == 'space':
                    delimiter = ' '
                elif delim_name == 'comma':
                    delimiter = ','
                elif delim_name == 'semicolon':
                    delimiter = ';'
                else:
                    delimiter = delim_name
                    
        elif line.startswith('#COMMENT'):
            # Parse comment command: #COMMENT !
            parts = line.split(maxsplit=1)
            if len(parts) >= 2:
                comment_char = parts[1].strip()
                
        elif line.startswith('#'):
            # Unrecognized command
            raise ValueError(f'Unrecognized command: {line}')
        else:
            # Regular data line
            if comment_char and line.startswith(comment_char):
                continue  # Skip commented data lines
            rows.append(line)
    
    # Apply skip_rows
    if skip_rows > 0:
        rows = rows[skip_rows:]
    
    # Parse rows with delimiter
    parsed_rows = []
    for row in rows:
        parsed_rows.append([cell.strip() for cell in row.split(delimiter)])
    
    return {
        'rows': parsed_rows,
        'skip': skip_rows,
        'delimiter': delimiter,
        'comment_char': comment_char
    }
