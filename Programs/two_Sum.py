import argparse

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--required-tag")
parser.add_argument("--commit-id")
parser.add_argument("--services")
args = parser.parse_args()

# Extract command-line arguments
required_tag = args.required_tag
commit_id = args.commit_id
services = args.services

# Print the extracted arguments
print("Required Tag:", required_tag)
print("Commit ID:", commit_id)
print("Services:", services)

# Split arguments into arrays
required_tag_array = required_tag.split(" ")
services_array = services.split(" ")

# Check each service for the required tags
for service in services_array:
    print(f"Checking tags for service: {service}")

    # Assume some logic for checking tags locally
    # Here, we are just printing a sample message
    for tag in required_tag_array:
        print(f"Checking if tag '{tag}' is present for Commit ID: {commit_id} in repository: {service}")

print("Local check completed.")
