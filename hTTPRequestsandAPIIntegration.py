import requests

def fetch_api_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # URL of the API endpoint
    api_url = 'https://reqres.in/api/users?page=2'
    api_data = fetch_api_data(api_url)
    if api_data:
        print("Received API data:", api_data)
