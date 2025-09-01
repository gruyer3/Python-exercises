# Script flow can be controlled based on conditions using if, elif and else statements

# if statement executes a block of code only if a condition is True
server_status = "running"
if server_status == "running":
    print ("Service is running")

# python treats many values as truthy or falsy in conditionals
# falsy: False, None, 0, 0.0, '', [], {}
# truthy: non-zero numbers, non-empty sequences or collections
servers = ["web01", "web02"]
error_message = ""
default_config = {}
if servers:
    print (f"Processing {len(servers)} servers.")
if error_message:
    print ("Something went wrong:", error_message)
if not default_config:
    print ("Default config not available, please provide the configuration values.")

# else is used to execute the code when the if condition is False
cpu_usage = 85.0
if cpu_usage > 90.0:
    print ("ALERT: High CPU Usage")
else:
    print ("CPU usage is normal.")

# elif chain multiple checks, the first true blocks run
http_status = 404
if http_status == 200:
    print ("Status OK")
elif http_status == 404:
    print ("Resource not found")
elif http_status >= 500:
    print ("Server error (5xx)")
else:
    print ("Another status:", http_status)