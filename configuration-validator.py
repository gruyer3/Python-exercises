# Function that validates a configuration dictionary before deployment process begins
def validate_config(config: dict) -> bool:
    """
    Validates a configuration dictionary against a set of rules.
    """
    # 1. Check for the presence of all required keys
    required_keys = ['service_name', 'env', 'port']
    for key in required_keys:
        if key not in config:
            return False
 
    # 2. Validate the 'env' value
    allowed_envs = {'dev', 'staging', 'prod'}
    if config['env'] not in allowed_envs:
        return False
 
    # 3. Validate 'service_name' is a non-empty string
    if not isinstance(config['service_name'], str) or not config['service_name']:
        return False
 
    # 4. Validate 'port' type and range
    port = config['port']
    if not isinstance(port, int):
        return False
    if not (1 <= port <= 65535):
        return False
 
    # 5. If all checks pass, the config is valid
    return True