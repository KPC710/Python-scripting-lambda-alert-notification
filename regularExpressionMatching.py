import re

def extract_email_addresses(text):
    emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
    return emails

# Example usage
if __name__ == "__main__":
    # Text containing email addresses
    sample_text = "Contact us at info@example.com or support@example.org"
    extracted_emails = extract_email_addresses(sample_text)
    print("Extracted emails:", extracted_emails)
