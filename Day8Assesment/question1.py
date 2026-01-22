import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Demo/1.0"
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()
    data = response.json()
    extracted_users = []

    for user in data:
        extracted_users.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city")
        })

    with open("users_data.json", "w") as file:
        json.dump(extracted_users, file, indent=4)

    print("Data successfully fetched and saved to users_data.json")

except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the server")

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.RequestException as err:
    print("Unexpected error:", err)

except json.JSONDecodeError:
    print("Error decoding JSON response")
