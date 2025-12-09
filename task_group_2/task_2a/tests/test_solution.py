import pytest


def test_parse_csv_with_commands_exists():
    """Test that parse_csv_with_commands function exists."""
    from src.solution import parse_csv_with_commands
    assert callable(parse_csv_with_commands)


def test_uppercase_commands():
    """Test that UPPERCASE commands work (should always work)."""
    from src.solution import parse_csv_with_commands
    
    data = """#SKIP 1
#DELIMITER comma
Header
Alice,100
Bob,200"""
    
    result = parse_csv_with_commands(data)
    assert result['skip'] == 1
    assert result['delimiter'] == ','
    assert len(result['rows']) == 2


def test_lowercase_commands():
    """Test THE BUG: lowercase commands should work but don't."""
    from src.solution import parse_csv_with_commands
    
    data = """#skip 2
#delimiter tab
Header1
Header2
Alice	100
Bob	200"""
    
    result = parse_csv_with_commands(data)
    assert result['skip'] == 2
    assert result['delimiter'] == '\t'
    assert len(result['rows']) == 2
    assert result['rows'][0] == ['Alice', '100']


def test_mixed_case_commands():
    """Test that MixedCase commands work."""
    from src.solution import parse_csv_with_commands
    
    data = """#Skip 1
#Delimiter semicolon
Header
Alice;100
Bob;200"""
    
    result = parse_csv_with_commands(data)
    assert result['skip'] == 1
    assert result['delimiter'] == ';'
    assert len(result['rows']) == 2


def test_comment_command_lowercase():
    """Test lowercase #comment command."""
    from src.solution import parse_csv_with_commands
    
    data = """#comment !
! This is a comment
Alice,100
Bob,200"""
    
    result = parse_csv_with_commands(data)
    assert result['comment_char'] == '!'
    assert len(result['rows']) == 2  # Comment line excluded


def test_all_delimiter_types():
    """Test different delimiter types with lowercase commands."""
    from src.solution import parse_csv_with_commands
    
    # Test tab
    data1 = """#delimiter tab
Alice	100"""
    result1 = parse_csv_with_commands(data1)
    assert result1['delimiter'] == '\t'
    
    # Test space
    data2 = """#delimiter space
Alice 100"""
    result2 = parse_csv_with_commands(data2)
    assert result2['delimiter'] == ' '
    
    # Test semicolon
    data3 = """#delimiter semicolon
Alice;100"""
    result3 = parse_csv_with_commands(data3)
    assert result3['delimiter'] == ';'


def test_realistic_qdp_style():
    """Test realistic file similar to QDP format (the original bug report)."""
    from src.solution import parse_csv_with_commands
    
    # This is similar to the reported bug in astropy
    data = """#skip 1
#delimiter space
Time Flux Error
1.5 10.2 0.5
2.3 11.4 0.6"""
    
    result = parse_csv_with_commands(data)
    assert result['skip'] == 1
    assert result['delimiter'] == ' '
    assert len(result['rows']) == 2
    assert result['rows'][0] == ['1.5', '10.2', '0.5']


def test_unrecognized_command_still_raises():
    """Test that truly unrecognized commands still raise errors."""
    from src.solution import parse_csv_with_commands
    
    data = """#invalid_command 123
Alice,100"""
    
    with pytest.raises(ValueError, match="Unrecognized command"):
        parse_csv_with_commands(data)


def test_no_commands():
    """Test CSV without any commands."""
    from src.solution import parse_csv_with_commands
    
    data = """Alice,100
Bob,200"""
    
    result = parse_csv_with_commands(data)
    assert result['skip'] == 0
    assert result['delimiter'] == ','
    assert len(result['rows']) == 2


def test_empty_lines_ignored():
    """Test that empty lines are handled correctly."""
    from src.solution import parse_csv_with_commands
    
    data = """#skip 1

Header

Alice,100

Bob,200
"""
    
    result = parse_csv_with_commands(data)
    assert len(result['rows']) == 2
