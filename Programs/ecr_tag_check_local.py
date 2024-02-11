import argparse

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--required-tag", nargs="+")
parser.add_argument("--commit-id")
parser.add_argument("--services", nargs="+")
args = parser.parse_args()

# Extract command-line arguments
required_tag_array = args.required_tag
commit_id = args.commit_id
services_array = args.services

# Print the extracted arguments
print("Required Tag:", required_tag_array)
print("Commit ID:", commit_id)
print("Services:", services_array)

# Check each service for the required tags
for service in services_array:
    print(f"Checking tags for service: {service}")

    # Assume some logic for checking tags locally
    # Here, we are just printing a sample message
    for tag in required_tag_array:
        print(f"Checking if tag '{tag}' is present for Commit ID: {commit_id} in repository: {service}")

print("Local check completed.")
