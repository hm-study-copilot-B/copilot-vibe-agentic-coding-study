"""
Demo script for JSON configuration validator.
Run this to see the validator in action (after fixing the bug).
"""

from solution import validate_config


def demo_working_types():
    """Demo: Types that already work (int, float, str)."""
    print("\n1. Working types (int, float, str)")
    
    schema = {
        "name": "str",
        "port": "int",
        "timeout": "float"
    }
    
    config = {
        "name": "MyApp",
        "port": "8080",      # String will convert to int
        "timeout": "30.5"    # String will convert to float
    }
    
    try:
        result = validate_config(config, schema)
        print(f"   ✓ Validated successfully")
        print(f"   Result: {result}")
        print(f"   Types: port={type(result['port']).__name__}, timeout={type(result['timeout']).__name__}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


def demo_boolean_bug():
    """Demo: Boolean type (THE BUG - doesn't work)."""
    print("\n2. Boolean type (THE BUG)")
    
    schema = {
        "debug": "bool",
        "enabled": "bool"
    }
    
    config = {
        "debug": "true",     # Should convert to True
        "enabled": "false"   # Should convert to False
    }
    
    try:
        result = validate_config(config, schema)
        print(f"   ✓ Validated successfully")
        print(f"   Result: {result}")
        print(f"   Types: debug={type(result['debug']).__name__}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")
        print(f"   ✗ BUG: Boolean conversion not implemented!")


def demo_case_insensitive():
    """Demo: Boolean values should be case-insensitive."""
    print("\n3. Case-insensitive boolean values")
    
    schema = {
        "flag1": "bool",
        "flag2": "bool",
        "flag3": "bool"
    }
    
    config = {
        "flag1": "True",     # Capitalized
        "flag2": "FALSE",    # All caps
        "flag3": "1"         # Numeric string
    }
    
    try:
        result = validate_config(config, schema)
        print(f"   ✓ Validated successfully")
        print(f"   Result: {result}")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


def demo_realistic_config():
    """Demo: Realistic application configuration."""
    print("\n4. Realistic application config")
    
    schema = {
        "app_name": "str",
        "debug": "bool",
        "port": "int",
        "timeout": "float",
        "auto_reload": "bool"
    }
    
    # Config from environment variables (all strings)
    config = {
        "app_name": "WebServer",
        "debug": "true",
        "port": "8080",
        "timeout": "30.0",
        "auto_reload": "false"
    }
    
    try:
        result = validate_config(config, schema)
        print(f"   ✓ Validated successfully")
        print(f"   Result:")
        for key, value in result.items():
            print(f"     {key}: {value} ({type(value).__name__})")
    except ValueError as e:
        print(f"   ✗ Error: {e}")


def demo_missing_field():
    """Demo: Missing required field still raises error."""
    print("\n5. Missing required field (should still fail)")
    
    schema = {
        "required_field": "str",
        "another_field": "int"
    }
    
    config = {
        "required_field": "value"
        # missing another_field
    }
    
    try:
        result = validate_config(config, schema)
        print(f"   ✗ Should have raised error for missing field!")
    except ValueError as e:
        print(f"   ✓ Correctly raised error: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("JSON Configuration Validator Demo")
    print("=" * 60)
    
    demo_working_types()
    demo_boolean_bug()
    demo_case_insensitive()
    demo_realistic_config()
    demo_missing_field()
    
    print("\n" + "=" * 60)
    print("Fix the boolean conversion bug in solution.py!")
    print("=" * 60)
