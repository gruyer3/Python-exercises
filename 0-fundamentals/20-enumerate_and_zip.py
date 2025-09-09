# use enumerate(iterable, start=0) to get (index, item) pairs
# the start parameter sets the initial index value
servers = ["web01", "web02", "web03"]
for idx, server in enumerate(servers, 1):
    print(f"#{idx},: Processing server {server}")

# use zip(*iterables) to pair items from multiple iterables
# iteration stops when the shortest iterable is exhausted
hosts = ["hostA", "hostB", "hostC"]
ips = ["10.0.0.1", "10.0.0.2"]
azs = ["us-east-1a", "us-east-1b"]

for host, ip, az in zip(hosts, ips, azs):
    print(f"Host: {host}, IP:{ip}, AZ:{az}")