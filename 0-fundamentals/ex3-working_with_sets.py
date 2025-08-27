# Create a set of strings named required, representing possible required packages
# Include a few duplicates to practice set operations
# Test for membership of 'requests' and 'ansible' strings
# Add 'paramiko' and safely remove 'pip' from the set
# Create another set of strings, now named installed. Mention a few of the packages listed under the required set.
# Given these two sets, compute missing, extra and common packages.

required = {"pip", "requests", "python3", "boto3", "python3"}
print ("requests" in required)
print ("ansible" in required)

required.add("paramiko")
print(required)
required.discard("pip")
print(required)

installed = {"python3", "ansible", "docker"}

missing_packages = required.difference(installed)
print (missing_packages)

extra_packages = installed.difference(required)
print(extra_packages)

common_packages = (required & installed)
print(common_packages)
