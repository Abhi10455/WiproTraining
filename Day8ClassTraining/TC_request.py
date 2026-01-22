import requests

geturl = "https://api.restful-api.dev/objects"
response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())

posturl = "https://api.restful-api.dev/objects"

post_body = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

post_response = requests.post(posturl, json=post_body)
print("post status code", post_response.status_code)
post_data = post_response.json()
print(post_data)

object_id = post_data["id"]

puturl = f"https://api.restful-api.dev/objects/{object_id}"

put_body = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}

put_response = requests.put(puturl, json=put_body)
print("put status code", put_response.status_code)
print(put_response.json())

patch_body = {
    "name": "Apple MacBook Pro 16 (Updated Name)"
}

patch_response = requests.patch(puturl, json=patch_body)
print("patch status code", patch_response.status_code)
print(patch_response.json())

delete_response = requests.delete(puturl)
print("delete status code", delete_response.status_code)

if delete_response.text:
    print(delete_response.json())
else:
    print("Object deleted successfully")
