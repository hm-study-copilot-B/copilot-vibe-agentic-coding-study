"""
JSON Configuration Validator
BUGGY IMPLEMENTATION - Missing boolean type conversion!
"""


def validate_config(config, schema):
    """
    Validate a configuration dictionary against a schema.
    
    The schema defines expected types for each field. Values in config
    can be strings (common from environment variables or CLI args) and
    will be converted to the expected type.
    
    BUG: Missing conversion for boolean type! Only int and float are handled.
    
    Parameters:
    - config: Dictionary with configuration values (may contain strings)
    - schema: Dictionary mapping field names to expected types
              Types: 'str', 'int', 'float', 'bool'
    
    Returns:
    - Dictionary with validated and type-converted values
    
    Raises:
    - ValueError: If validation fails or conversion is not possible
    """
    validated = {}
    
    for key, expected_type in schema.items():
        if key not in config:
            raise ValueError(f'Missing required field: {key}')
        
        value = config[key]
        
        # Convert string values to expected types
        if isinstance(value, str):
            if expected_type == 'str':
                # Already a string, no conversion needed
                validated[key] = value
                
            elif expected_type == 'int':
                try:
                    validated[key] = int(value)
                except ValueError:
                    raise ValueError(f'Field {key}: cannot convert "{value}" to int')
                    
            elif expected_type == 'float':
                try:
                    validated[key] = float(value)
                except ValueError:
                    raise ValueError(f'Field {key}: cannot convert "{value}" to float')
            
            else:
                raise ValueError(f'Field {key}: unknown type "{expected_type}"')
        else:
            # Value is already the right Python type
            if expected_type == 'bool' and not isinstance(value, bool):
                raise ValueError(f'Field {key}: expected bool, got {type(value).__name__}')
            elif expected_type == 'int' and not isinstance(value, int):
                raise ValueError(f'Field {key}: expected int, got {type(value).__name__}')
            elif expected_type == 'float' and not isinstance(value, (int, float)):
                raise ValueError(f'Field {key}: expected float, got {type(value).__name__}')
            
            validated[key] = value
    
    return validated
