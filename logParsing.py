def parse_log_file(log_file_path, keyword):
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Path to log file and keyword to search
    log_path = 'path/to/logfile.log'
    search_keyword = 'ERROR'
    parse_log_file(log_path, search_keyword)
