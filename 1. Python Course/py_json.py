# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

json_es = '{"name":"emir", "age":21}'
x = json.loads(json_es)
print(json_es)

x["name"]="Emirhan"


json_es = json.dumps(x)
print(json_es)