import json
data={
    "name":"Ravi",
    "age":20,
    "skills":["python"]
}

with open("data.json","w") as file:
    json.dump(data,file)