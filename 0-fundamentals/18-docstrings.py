# the first string in a function is its docstring, explaining purpose, Args: and Returns:
# observing the following conventions is considered a good practice:
# 1. one-line summary
# 2. blank line
# 3. detailed description (optional)
# 4. Args: section for parameters
# 5. Returns: section for return values
# 6. Raises: section for exceptions

import socket

def check_port(host, port, timeout=5):
    """Checks if a TCP port is open on a given host.
    
    Provide a detailed description.

    Args:
        host(str): Hostname or IP address
        port(int): TCP port number
        timeout(int, optional): Connection timeout in seconds. Defaults to 5.
        
    Returns:
        bool: True if the port is open, False otherwise.
    """
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except Exception:
        return False
    
print (check_port("www.google.com", 443))
print (check_port("www.sdasdasdasdasdasd.com", 22))