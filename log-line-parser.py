def parse_log_line(log_line: str) -> dict | None:
    
    # Guard clause for empty or None input
    if not isinstance(log_line, str) or not log_line:
        return None
 
    # Split the log line into a maximum of three parts.
    # This correctly handles messages that contain spaces.
    parts = log_line.split(' ', 2)
 
    # A valid log line must have at least 3 parts: timestamp, log level, and message.
    if len(parts) < 3:
        return None
 
    timestamp, log_level_raw, message = parts
 
    # The log level should be enclosed in brackets (e.g., "[INFO]")
    # and be at least 3 characters long (e.g., "[A]")
    if not (log_level_raw.startswith('[') and log_level_raw.endswith(']')):
        return None
 
    # Strip the brackets from the log level
    log_level = log_level_raw.strip('[]')
 
    # Construct and return the dictionary
    return {
        'timestamp': timestamp,
        'log_level': log_level,
        'message': message
    }