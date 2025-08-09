import requests

# A simple URL that is always online
url_to_test = "https://www.google.com"

# Standard browser headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"--- Starting Connection Test ---")
print(f"Attempting to connect to: {url_to_test}")

try:
    # Try to make the web request
    response = requests.get(url_to_test, headers=headers, timeout=10)

    # Check if the HTTP request was successful
    response.raise_for_status()

    print("\n✅ SUCCESS!")
    print(f"Successfully connected. The server responded with status code: {response.status_code}")

except requests.RequestException as e:
    # This block will run if the connection fails for any reason
    print("\n❌ FAILED!")
    print("The script was blocked from accessing the internet.")
    print("This is likely due to a Firewall, Antivirus, or network proxy setting.")
    print(f"\nDetailed Error: {e}")

print(f"--- Test Finished ---")