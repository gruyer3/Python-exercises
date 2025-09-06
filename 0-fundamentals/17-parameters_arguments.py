# parameters are named in the def signature; arguments are the actual values passed when calling
# positional args match by order; keyword args match by name and can be out of order
# positional arguments must come first
def check_service_status(service_name, expected_status):
    print(f"Checking {service_name} for {expected_status}...")
    return True

check_service_status("running", "nginx")
check_service_status("nginx", "running")

# it is possible to give parameters default values in the signature (param=default), making them optional
def connect(host, port=22, timeout=30):
    print (f"Connect to host {host} on port {port} (timeout {timeout})")

connect("web01")
connect("web02", 443, 60)
# when wanting to set the value of timeout but use the default value of port
# we need to use keyword arguments, since positional arguments would be incorrectly mapped
connect("web03", timeout=120)