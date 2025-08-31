# Create a server_info dict with keys 'id', 'ip_address', 'state' and 'tags' 
server_info = {
    "id": "web01",
    "ip_address": "192.168.0.120",
    "state": "running",
    "tags": {
        "environment": "production",
        "owner": "engineering"
    }
}
# Print the server's 'state'
print ("Server state:", server_info.get("state"))
# Safely get 'instance_type' with defaut 't2.micro'
instance_type = server_info.get("instance_type", "t2.micro")
print ("Instance type:", instance_type)
# Change 'state' to 'stopped'
server_info["state"] = "stopped"
print (server_info)
# Add a new tag to 'tags' dictionary
server_info["tags"]["region"] = "eu-central-1"
print (server_info)
# Iterate over the directory with .items() to display key-value pairs
for key, value in server_info.items():
    print (f"- {key}: {value}")