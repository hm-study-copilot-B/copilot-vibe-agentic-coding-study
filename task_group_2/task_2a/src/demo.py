"""
Demo script for CSV parser with command support.
Run this to see the parser in action (after fixing the bug).
"""

from solution import parse_csv_with_commands


def demo_uppercase_commands():
    """Demo: File with UPPERCASE commands (works even with bug)."""
    print("\n1. CSV with UPPERCASE commands")
    
    data = """#SKIP 1
#DELIMITER comma
Name,Value,Status
Header Row to Skip
Alice,100,Active
Bob,200,Inactive"""
    
    try:
        result = parse_csv_with_commands(data)
        print(f"   ✓ Parsed successfully")
        print(f"   Skip: {result['skip']}, Delimiter: '{result['delimiter']}'")
        print(f"   Rows: {result['rows']}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


def demo_lowercase_commands():
    """Demo: File with lowercase commands (FAILS with bug)."""
    print("\n2. CSV with lowercase commands (THE BUG)")
    
    data = """#skip 2
#delimiter tab
Name	Value	Error
Row to skip 1
Row to skip 2
Alice	1.5	0.1
Bob	2.3	0.2"""
    
    try:
        result = parse_csv_with_commands(data)
        print(f"   ✓ Parsed successfully")
        print(f"   Skip: {result['skip']}, Delimiter: '{result['delimiter']}'")
        print(f"   Rows: {result['rows']}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")
        print(f"   ✗ BUG: lowercase commands should work!")


def demo_mixed_case():
    """Demo: File with MixedCase commands."""
    print("\n3. CSV with MixedCase commands")
    
    data = """#Skip 1
#Delimiter semicolon
#Comment !
! This line is commented out
Name;Value;Status
Header
Alice;100;Active
Bob;200;Inactive"""
    
    try:
        result = parse_csv_with_commands(data)
        print(f"   ✓ Parsed successfully")
        print(f"   Skip: {result['skip']}, Delimiter: '{result['delimiter']}'")
        print(f"   Comment char: '{result['comment_char']}'")
        print(f"   Rows: {result['rows']}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


def demo_realistic_data():
    """Demo: Realistic scientific data file."""
    print("\n4. Realistic data file (like QDP format)")
    
    data = """#skip 1
#delimiter space
Time Flux Error
Units: days mJy mJy
1.5 10.2 0.5
2.3 11.4 0.6
3.1 9.8 0.4"""
    
    try:
        result = parse_csv_with_commands(data)
        print(f"   ✓ Parsed successfully")
        print(f"   Data rows: {len(result['rows'])}")
        for row in result['rows']:
            print(f"     {row}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("CSV Parser with Commands Demo")
    print("=" * 60)
    
    demo_uppercase_commands()
    demo_lowercase_commands()
    demo_mixed_case()
    demo_realistic_data()
    
    print("\n" + "=" * 60)
    print("Fix the case-sensitivity bug in solution.py!")
    print("=" * 60)
