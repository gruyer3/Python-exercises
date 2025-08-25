# Create a list called deployment_targets with values ['us-east-1', 'eu-west-1', 'ap-southeast-2']
deployment_targets = ['us-east-1', 'eu-west-1', 'ap-southeast-2']
print (deployment_targets)
# Print the first target
print (deployment_targets[0])
# Append 'us-west-2'
deployment_targets.append('us-west-2')
print (deployment_targets)
# Change the second element to 'eu-central-1'
deployment_targets.insert(1, 'eu-central-1')
print (deployment_targets)
# Print the list after each step