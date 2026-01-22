import requests

geturl = "http://127.0.0.1:5000/users"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Client"
}

response = requests.get(geturl, headers=headers, timeout=10)
print("get status code", response.status_code)
print(response.json())

posturl = " http://127.0.0.1:5000/users"

post_body = {
    "name": "sai"
}

post_response = requests.post(posturl, json=post_body)
print("post status code", post_response.status_code)

post_data = post_response.json()
print(post_data)

object_id = post_data["id"]

puturl = "http://127.0.0.1:5000/users/2"

put_body = {
    "name": "abhi"
}

put_response = requests.put(puturl, json=put_body)
print("put status code", put_response.status_code)
print(put_response.json())


