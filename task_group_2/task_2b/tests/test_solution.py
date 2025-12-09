import pytest


def test_validate_config_exists():
    """Test that validate_config function exists."""
    from src.solution import validate_config
    assert callable(validate_config)


def test_string_type():
    """Test string type validation."""
    from src.solution import validate_config
    
    schema = {"name": "str"}
    config = {"name": "TestApp"}
    
    result = validate_config(config, schema)
    assert result['name'] == "TestApp"
    assert isinstance(result['name'], str)


def test_int_type_conversion():
    """Test int type conversion from string."""
    from src.solution import validate_config
    
    schema = {"port": "int"}
    config = {"port": "8080"}
    
    result = validate_config(config, schema)
    assert result['port'] == 8080
    assert isinstance(result['port'], int)


def test_float_type_conversion():
    """Test float type conversion from string."""
    from src.solution import validate_config
    
    schema = {"timeout": "float"}
    config = {"timeout": "30.5"}
    
    result = validate_config(config, schema)
    assert result['timeout'] == 30.5
    assert isinstance(result['timeout'], float)


def test_bool_type_lowercase_true():
    """Test THE BUG: boolean "true" should convert to True."""
    from src.solution import validate_config
    
    schema = {"debug": "bool"}
    config = {"debug": "true"}
    
    result = validate_config(config, schema)
    assert result['debug'] is True
    assert isinstance(result['debug'], bool)


def test_bool_type_lowercase_false():
    """Test THE BUG: boolean "false" should convert to False."""
    from src.solution import validate_config
    
    schema = {"enabled": "bool"}
    config = {"enabled": "false"}
    
    result = validate_config(config, schema)
    assert result['enabled'] is False
    assert isinstance(result['enabled'], bool)


def test_bool_type_uppercase():
    """Test boolean with uppercase strings."""
    from src.solution import validate_config
    
    schema = {"flag1": "bool", "flag2": "bool"}
    config = {"flag1": "TRUE", "flag2": "FALSE"}
    
    result = validate_config(config, schema)
    assert result['flag1'] is True
    assert result['flag2'] is False


def test_bool_type_mixed_case():
    """Test boolean with mixed case strings."""
    from src.solution import validate_config
    
    schema = {"flag1": "bool", "flag2": "bool"}
    config = {"flag1": "True", "flag2": "False"}
    
    result = validate_config(config, schema)
    assert result['flag1'] is True
    assert result['flag2'] is False


def test_bool_type_numeric_strings():
    """Test boolean with numeric strings."""
    from src.solution import validate_config
    
    schema = {"flag1": "bool", "flag2": "bool"}
    config = {"flag1": "1", "flag2": "0"}
    
    result = validate_config(config, schema)
    assert result['flag1'] is True
    assert result['flag2'] is False


def test_bool_type_empty_string():
    """Test boolean with empty string (should be False)."""
    from src.solution import validate_config
    
    schema = {"flag": "bool"}
    config = {"flag": ""}
    
    result = validate_config(config, schema)
    assert result['flag'] is False


def test_mixed_types():
    """Test configuration with all type combinations."""
    from src.solution import validate_config
    
    schema = {
        "app_name": "str",
        "debug": "bool",
        "port": "int",
        "timeout": "float",
        "enabled": "bool"
    }
    
    config = {
        "app_name": "WebServer",
        "debug": "true",
        "port": "8080",
        "timeout": "30.0",
        "enabled": "false"
    }
    
    result = validate_config(config, schema)
    assert result['app_name'] == "WebServer"
    assert result['debug'] is True
    assert result['port'] == 8080
    assert result['timeout'] == 30.0
    assert result['enabled'] is False


def test_missing_field_raises_error():
    """Test that missing required field raises ValueError."""
    from src.solution import validate_config
    
    schema = {"required_field": "str", "another_field": "int"}
    config = {"required_field": "value"}  # missing another_field
    
    with pytest.raises(ValueError, match="Missing required field"):
        validate_config(config, schema)


def test_invalid_int_conversion():
    """Test that invalid int conversion raises ValueError."""
    from src.solution import validate_config
    
    schema = {"port": "int"}
    config = {"port": "not_a_number"}
    
    with pytest.raises(ValueError, match="cannot convert"):
        validate_config(config, schema)


def test_invalid_float_conversion():
    """Test that invalid float conversion raises ValueError."""
    from src.solution import validate_config
    
    schema = {"timeout": "float"}
    config = {"timeout": "not_a_number"}
    
    with pytest.raises(ValueError, match="cannot convert"):
        validate_config(config, schema)


def test_already_correct_type():
    """Test values that are already the correct Python type."""
    from src.solution import validate_config
    
    schema = {"port": "int", "debug": "bool"}
    config = {"port": 8080, "debug": True}  # Already correct types
    
    result = validate_config(config, schema)
    assert result['port'] == 8080
    assert result['debug'] is True


def test_realistic_environment_variables():
    """Test realistic scenario with environment variables (all strings)."""
    from src.solution import validate_config
    
    # Simulating environment variables - all strings
    schema = {
        "DATABASE_URL": "str",
        "DEBUG": "bool",
        "MAX_CONNECTIONS": "int",
        "TIMEOUT_SECONDS": "float",
        "AUTO_RELOAD": "bool"
    }
    
    config = {
        "DATABASE_URL": "postgres://localhost/db",
        "DEBUG": "true",
        "MAX_CONNECTIONS": "100",
        "TIMEOUT_SECONDS": "30.5",
        "AUTO_RELOAD": "false"
    }
    
    result = validate_config(config, schema)
    assert isinstance(result['DATABASE_URL'], str)
    assert isinstance(result['DEBUG'], bool)
    assert isinstance(result['MAX_CONNECTIONS'], int)
    assert isinstance(result['TIMEOUT_SECONDS'], float)
    assert isinstance(result['AUTO_RELOAD'], bool)
