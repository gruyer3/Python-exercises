server_name = "webserver-03"
cpu_cores = 4 
memory_gb = 8.0
disk_total_gb = 500
disk_used_gb = 350

# Compute the disk usage percentage.
disk_usage_percentage = disk_used_gb / disk_total_gb
# Print raw percentage value.
print (disk_usage_percentage)
# Build a human readable summary string:
#   - Convert server name to uppercase.
server_name_upper = server_name.upper()
#   - Include the number of CPU cores and amount of RAM.
#   - Show the disk usage percentage rounded to one decimal place.
summary = (f"{server_name_upper}: CPU_cores:{cpu_cores} Memory:{memory_gb} Disk_usage:{disk_usage_percentage:.2%}")
print (summary)
# Print a summary containing the server name in uppercase, the number of CPU cores, the memory, and the disk usage.
# Use the .2% format specifier in an f-string to display the usage with two decimal places and a percent sign.

