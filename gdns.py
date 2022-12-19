import json
import requests

token = ""
domain = ""
sub = ""
type = "A"

api_base = "https://api.gcorelabs.com/dns/v2/zones/"
APIKey = "APIKey " + token
headers = {"Authorization": APIKey}

def get_record():
    url = api_base + domain + "/" + sub + "." + domain + "/" + type
    result = requests.get(url, headers=headers)
    if str(result.text).find("error") >= 0:
        print("未找到子域，执行创建")
        data = {"filters":[{"type":"default"}],"resource_records":[{"content":["0.0.0.0"]}], "ttl": 60}
        requests.post(url, data=data)
        return "0"
    return json.loads(result.text)["resource_records"][0]["content"][0]
    

def update_record(ip):
    url = api_base + domain + "/" + sub + "." + domain + "/" + type
    data = {"resource_records":[{"content":[ip]}], "ttl": 300}
    result = requests.put(url, headers=headers, json=data)
    print(result.text)

local_ip = requests.get("http://ifconfig.me")
if local_ip.text != get_record():
    print("执行更新")
    update_record(local_ip.text)
else:
    print("无需更新")
