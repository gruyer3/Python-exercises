# break: immediately exits the innermost loop, useful when you've found what you need or hit an error
users = ["guest", "tester", "admin01", "admin02", "dev01"]
found_admin = None

for user in users:
    print (f"Checking users: {user}")
    if user.startswith("admin"):
        found_admin = user
        print (f"Admin user found: {found_admin}. Stopping search")
        break

# continue: skips the rest of the current interation and moves to the next one, useful for skipping items that don't meet criteria
filenames = ["nginx.conf", "app.yaml", "db.yaml", "notex.txt"]

for file in filenames:
    if not file.endswith(".yaml"):
        print (f"Skipping non-yaml file: {file}")
        continue
    print (f"Processing YAML config {file}")